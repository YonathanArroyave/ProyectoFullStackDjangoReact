import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { getConsultas, calculateStatistics } from '../api/consultas';
import Sidebar from '../components/Sidebar';
import DashboardHeader from '../components/DashboardHeader';
import MetricCardCompact from '../components/MetricCardCompact';
import LoadingSpinner from '../components/LoadingSpinner';
import { toast } from 'react-hot-toast';
import '/src/output.css';

const Dashboard = () => {
  const [planesPendientes, setPlanesPendientes] = useState(0);
  const [loading, setLoading] = useState(true);
  const [stats, setStats] = useState({
    totalAtendidosMes: 0,
    totalAtendidosAno: 0,
    totalRecursosMes: 0,
    totalRecursosAno: 0,
    error: null
  });
  const navigate = useNavigate();

  useEffect(() => {
    const loadData = async () => {
      try {
        const consultas = await getConsultas();

        const pendientes = consultas.filter(c => !c.envio_plan).length;
        setPlanesPendientes(pendientes);

        const calculatedStats = calculateStatistics(consultas);
        
        setStats({
          ...calculatedStats,
          error: null
        });

      } catch (error) {
        if (error.message === 'SESSION_EXPIRED') {
          toast.error('Sesión expirada. Por favor ingresa nuevamente');
          navigate('/login');
        } else {
          setStats(prev => ({
            ...prev,
            error: 'Error al cargar los datos. Intenta recargando la página.'
          }));
        }
      } finally {
        setLoading(false);
      }
    };

    loadData();
  }, [navigate]);

  return (
    <div className="flex min-h-screen bg-gray-50 dark:bg-gray-900">
      <Sidebar />
      
      <div className="flex-1 p-8 ml-64">
        <div className="max-w-7xl mx-auto">
          <DashboardHeader />
          
          {stats.error && (
            <div className="mb-8 p-4 bg-red-100 text-red-700 rounded-lg dark:bg-red-900 dark:text-red-100">
              {stats.error}
            </div>
          )}

          <div className="grid grid-cols-1 lg:grid-cols-4 gap-8">
            {/* Sección Principal simplificada */}
            <div className="lg:col-span-3">
              <div className="bg-white dark:bg-gray-800 p-8 rounded-2xl shadow-lg border border-gray-100 dark:border-gray-700">
                <h2 className="text-2xl font-semibold mb-6 dark:text-white">Resumen General</h2>
                
                {loading ? (
                  <LoadingSpinner />
                ) : (
                  <div className="space-y-4">
                    
                      
                  </div>
                )}
              </div>
            </div>

            {/* Sección Métricas (sin cambios) */}
            <div className="lg:col-span-1">
              <div className="bg-blue-50 dark:bg-gray-800 p-6 rounded-2xl shadow-lg border border-blue-100 dark:border-gray-700">
                <h3 className="text-xl font-semibold mb-6 dark:text-white">Métricas</h3>
                <div className="space-y-6">
                  <MetricCardCompact
                    title="Facturación del Mes:"
                    value={stats.totalRecursosMes.toLocaleString('es-CO', {
                      style: 'currency',
                      currency: 'COP',
                      minimumFractionDigits: 0
                    })}
                    percentage="+21%"
                  />
                  <MetricCardCompact
                    title="Dietas Pendientes:"
                    value={planesPendientes}
                    percentage="+54%"
                  />
                  <MetricCardCompact
                    title="Pacientes este año:"
                    value={stats.totalAtendidosAno}
                    percentage="+43%"
                  />
                  <MetricCardCompact
                    title="Pacientes este mes:"
                    value={stats.totalAtendidosMes}
                    percentage="+5%"
                  />
                  <MetricCardCompact
                    title="Ingresos en lo que va del Mes:"
                    value={stats.totalRecursosAno.toLocaleString('es-CO', {
                      style: 'currency',
                      currency: 'COP',
                      minimumFractionDigits: 0
                    })}
                    percentage="+5%"
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;