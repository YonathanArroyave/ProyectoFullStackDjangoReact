import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

const LogoutPage = () => {
  const navigate = useNavigate();

  useEffect(() => {
    // Eliminar los tokens de sesión
    localStorage.removeItem('accessToken');
    localStorage.removeItem('refreshToken');

    // Redirigir al login después de 2 segundos
    const timeout = setTimeout(() => {
      navigate('/'); // Redirige al login
    }, 2000);

    // Limpiar el timeout al desmontar el componente
    return () => clearTimeout(timeout);
  }, [navigate]);

  return (
    <div>
      <h2>Cerrando Sesión...</h2>
      <p>Espere un momento mientras se cierra su sesión.</p>
    </div>
  );
};

export default LogoutPage;
