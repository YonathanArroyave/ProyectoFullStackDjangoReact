import React, { useEffect, useState } from 'react';
import { Navigate } from 'react-router-dom';
import { refreshAccessToken, isAuthenticated } from '../api/auth';

const ProtectedRoute = ({ children }) => {
  const [loading, setLoading] = useState(true);
  const [isAuth, setIsAuth] = useState(false);

  useEffect(() => {
    const checkAuth = async () => {
      try {
        if (!isAuthenticated()) throw new Error('No autenticado');
        await refreshAccessToken(); // Intenta refrescar el token si es necesario
        setIsAuth(true);
      } catch (error) {
        console.error('Error de autenticación:', error);
        setIsAuth(false);
      } finally {
        setLoading(false);
      }
    };
    checkAuth();
  }, []);

  if (loading) return <div>Cargando...</div>; // Muestra un indicador de carga
  if (!isAuth) return <Navigate to="/" replace />;
  return children;
};

export default ProtectedRoute;
