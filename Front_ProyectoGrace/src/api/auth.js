import axios from 'axios';

// URL base de la API
const API_URL = 'http://127.0.0.1:8000/api'; // Ajusta según tu configuración

// Cliente Axios configurado
const api = axios.create({
  baseURL: API_URL,
});

// Función para iniciar sesión
export const login = async (email, password) => {
  try {
    const response = await api.post('/auth/login/', { email, password });
    return response.data; // Debería incluir los tokens 'access' y 'refresh'
  } catch (error) {
    throw new Error(error.response?.data?.detail || 'Error al iniciar sesión');
  }
};

// Función para verificar si el usuario está autenticado
export const isAuthenticated = () => {
  const token = localStorage.getItem('accessToken');
  return !!token; // Retorna true si hay un token, false si no
};

// Función para refrescar el token de acceso
export const refreshAccessToken = async () => {
  try {
    const refreshToken = localStorage.getItem('refreshToken');
    const accessToken = localStorage.getItem('accessToken');

    if (!refreshToken || !accessToken) throw new Error('Faltan tokens');

    const response = await api.post(
      '/api/token/refresh/',
      { refresh: refreshToken },
      {
        headers: {
          Authorization: `Bearer ${accessToken}`,
        },
      }
    );

    const { access } = response.data;
    localStorage.setItem('accessToken', access); // Actualiza el token en localStorage
    return access;
  } catch (error) {
    console.error('Error al refrescar el token:', error);
    throw error;
  }
};

// Interceptor para manejar errores de autenticación
api.interceptors.response.use(
  (response) => response, // Deja pasar las respuestas exitosas
  async (error) => {
    const originalRequest = error.config;

    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true; // Marca que esta es la primera vez que reintentamos
      try {
        const newAccessToken = await refreshAccessToken();
        api.defaults.headers.common['Authorization'] = `Bearer ${newAccessToken}`;
        originalRequest.headers['Authorization'] = `Bearer ${newAccessToken}`;
        return api(originalRequest); // Reintenta la solicitud original
      } catch (refreshError) {
        localStorage.removeItem('accessToken');
        localStorage.removeItem('refreshToken');
        window.location.href = '/'; // Redirige al login si falla el refresh
        return Promise.reject(refreshError);
      }
    }

    return Promise.reject(error);
  }
);

// Exporta el cliente Axios configurado
export default api;
