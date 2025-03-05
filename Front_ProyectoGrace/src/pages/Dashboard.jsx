import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { getConsultas, calculateStatistics } from '../api/consultas';
import Sidebar from '../components/Sidebar';
import DashboardHeader from '../components/DashboardHeader';
import MetricCardCompact from '../components/MetricCardCompact';
import '/src/output.css';

const Dashboard = () => {
  const [planesPendientes, setPlanesPendientes] = useState(0);
  const [loading, setLoading] = useState(true);
  const [stats, setStats] = useState({
    totalAtendidosMes: 0,
    totalAtendidosAno: 0,
    totalRecursosMes: 0,
    totalRecursosAno: 0,
  });
  const navigate = useNavigate();

  useEffect(() => {
    const fetchData = async () => {
      try {
        const consultas = await getConsultas();

        // Calcular planes pendientes
        const pendientes = consultas.filter((consulta) => consulta.envio_plan === false).length;
        setPlanesPendientes(pendientes);

        // Calcular estadísticas
        const statistics = calculateStatistics(consultas);
        setStats(statistics);
      } catch (error) {
        console.error('Error al cargar los datos:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  return (
    <div className="flex min-h-screen bg-gray-50 dark:bg-gray-900">
      <Sidebar />

      <div className="flex-1 p-8 ml-64"> {/* Aumentamos margen izquierdo */}
        <div className="max-w-7xl mx-auto"> {/* Contenedor más ancho */}
          <DashboardHeader />

          <div className="grid grid-cols-1 lg:grid-cols-4 gap-8"> {/* Nueva proporción 3:1 */}
            {/* Sección Principal */}
            <div className="lg:col-span-3"> {/* Ocupa 75% del ancho */}
              <div className="bg-white dark:bg-gray-800 p-8 rounded-2xl shadow-lg border border-gray-100 dark:border-gray-700">
                <h2 className="text-2xl font-semibold mb-6 dark:text-white">Bienvenida</h2>
                <div className="space-y-4">
                  <p className="text-lg text-gray-600 dark:text-gray-300 leading-relaxed">
                    Aquí puedes ver un resumen de tu actividad reciente...
                  </p>
                  <div className="grid grid-cols-2 gap-4 mt-6">
                    {/* Agrega más contenido aquí si es necesario */}
                  </div>
                </div>
              </div>
            </div>

            {/* Sección Métricas */}
            <div className="lg:col-span-1"> {/* 25% del ancho */}
              <div className="bg-blue-50 dark:bg-gray-800 p-6 rounded-2xl shadow-lg border border-blue-100 dark:border-gray-700">
                <h3 className="text-xl font-semibold mb-6 dark:text-white">Métricas</h3>
                <div className="space-y-6"> {/* Más espacio entre métricas */}
                  <MetricCardCompact
                    title="Facturación del Mes: "
                    value={stats.totalRecursosMes.toLocaleString('es-CO', {
                      style: 'currency',
                      currency: 'COP',
                      minimumFractionDigits: 0
                    })}
                    percentage="+21%"
                  />
                  <MetricCardCompact
                    title="Dietas Pendientes por enviar: "
                    value={planesPendientes}
                    percentage="+54%"
                  />
                  <MetricCardCompact
                    title="Total de Pacientes este año:"
                    value={stats.totalAtendidosAno}
                    percentage="+43%"
                  />
                  <MetricCardCompact
                    title="Pacientes Atendidos este mes: "
                    value={stats.totalAtendidosMes}
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