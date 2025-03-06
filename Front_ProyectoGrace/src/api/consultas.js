import api from './auth';

export const getConsultas = async () => {
  try {
    const response = await api.get('/consultas/');
    return response.data;
  } catch (error) {
    if (error.response?.status === 401) {
      console.error('Autenticación requerida');
      throw new Error('SESSION_EXPIRED');
    }
    console.error('Error en consultas:', error.message);
    throw new Error('Error al obtener los datos');
  }
};

export const calculateStatistics = (consultas) => {
  const currentDate = new Date();
  const currentMonth = currentDate.getMonth();
  const currentYear = currentDate.getFullYear();

  // Datos para el gráfico
  const monthlyData = Array(12).fill().map((_, index) => ({
    month: new Date(currentYear, index).toLocaleString('default', { month: 'short' }),
    count: 0
  }));

  const stats = consultas.reduce((acc, consulta) => {
    const fecha = new Date(consulta.fecha);
    const valor = parseFloat(consulta.valor) || 0;
    const monthIndex = fecha.getMonth();

    if (fecha.getFullYear() === currentYear) {
      acc.totalAtendidosAno += 1;
      acc.totalRecursosAno += valor;
      monthlyData[monthIndex].count += 1;

      if (fecha.getMonth() === currentMonth) {
        acc.totalAtendidosMes += 1;
        acc.totalRecursosMes += valor;
      }
    }
    return acc;
  }, {
    totalAtendidosMes: 0,
    totalAtendidosAno: 0,
    totalRecursosMes: 0,
    totalRecursosAno: 0,
    monthlyData: monthlyData
  });

  return stats;
};