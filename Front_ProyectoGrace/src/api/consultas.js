import api from './auth'; // Cliente Axios configurado con autenticación

// Función para obtener todas las consultas
export const getConsultas = async () => {
  try {
    const response = await api.get('/consultas/');
    return response.data;
  } catch (error) {
    console.error('Error al obtener las consultas:', error);
    throw error;
  }
};

// Función para calcular estadísticas
export const calculateStatistics = (consultas) => {
  const currentDate = new Date();
  const currentMonth = currentDate.getMonth(); // Mes actual (0-11)
  const currentYear = currentDate.getFullYear(); // Año actual

  let totalAtendidosMes = 0;
  let totalAtendidosAno = 0;
  let totalRecursosMes = 0;
  let totalRecursosAno = 0;

  consultas.forEach((consulta) => {
    const consultaFecha = new Date(consulta.fecha);
    const consultaValor = parseFloat(consulta.valor) || 0;

    if (consultaFecha.getFullYear() === currentYear) {
      totalAtendidosAno += 1;
      totalRecursosAno += consultaValor;

      if (consultaFecha.getMonth() === currentMonth) {
        totalAtendidosMes += 1;
        totalRecursosMes += consultaValor;
      }
    }
  });

  return {
    totalAtendidosMes,
    totalAtendidosAno,
    totalRecursosMes,
    totalRecursosAno,
  };
};
