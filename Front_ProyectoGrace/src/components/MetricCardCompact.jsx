import React from 'react';

const MetricCardCompact = ({ title, value, percentage }) => (
  <div className="bg-white dark:bg-gray-700 p-5 rounded-xl border border-gray-200 dark:border-gray-600">
    <div className="flex justify-between items-center">
      <span className="text-base font-medium text-gray-700 dark:text-gray-300">{title}</span>
      <div className="flex items-center gap-3">
        <span className="text-lg font-bold text-gray-900 dark:text-white">{value}</span>
        <span className="text-sm bg-green-100 text-green-800 px-3 py-1 rounded-full dark:bg-green-900 dark:text-green-200">
          {percentage}
        </span>
      </div>
    </div>
  </div>
);

export default MetricCardCompact; // Esta es la línea clave que faltaba