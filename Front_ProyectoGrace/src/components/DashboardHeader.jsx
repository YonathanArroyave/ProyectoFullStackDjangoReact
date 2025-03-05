import React, { useState, useEffect } from 'react';
import { Sun, Moon, Bell, User, Settings } from 'lucide-react';

const DashboardHeader = () => {
  const [isDarkMode, setIsDarkMode] = useState(false);
  const [notificationCount] = useState(3);

  useEffect(() => {
    if (isDarkMode) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }, [isDarkMode]);

  return (
    <header className="mb-8 flex items-center justify-between">
      {/* Título y subtítulo */}
      <div>
        <h1 className="text-2xl font-bold text-gray-800 dark:text-white">Bienvenida a Tu Dashboard</h1>
        <div className="mt-2 flex items-center gap-3 text-base text-gray-500 dark:text-gray-400">
          <span>Nutricionista</span>
          <span className="text-gray-400">•</span>
          <span>Grace Arroyave</span>
        </div>
      </div>

      {/* Controles del header */}
      <div className="flex items-center gap-6">
        <button
          onClick={() => setIsDarkMode(!isDarkMode)}
          className="p-2.5 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-xl transition-colors"
        >
          {isDarkMode ? (
            <Sun size={22} className="text-gray-600 dark:text-gray-300" />
          ) : (
            <Moon size={22} className="text-gray-600 dark:text-gray-300" />
          )}
        </button>

        <button className="p-2.5 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-xl relative">
          <Bell size={22} className="text-gray-600 dark:text-gray-300" />
          {notificationCount > 0 && (
            <span className="absolute top-0 right-0 bg-red-500 text-white text-xs px-2 py-1 rounded-full">
              {notificationCount}
            </span>
          )}
        </button>

        <button className="p-2.5 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-xl">
          <User size={22} className="text-gray-600 dark:text-gray-300" />
        </button>

        <button className="p-2.5 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-xl">
          <Settings size={22} className="text-gray-600 dark:text-gray-300" />
        </button>
      </div>
    </header>
  );
};

export default DashboardHeader;