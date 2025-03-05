import React from 'react';
import { Home, FileText, Users, Settings, LogOut, User } from 'lucide-react';

const Sidebar = () => {
  return (
    <aside className="w-64 bg-white border-r border-gray-200 dark:bg-gray-800 dark:border-gray-700 p-6 fixed h-full">
      {/* Sección Perfil */}
      <div className="flex items-center gap-4 mb-10">
        <div className="w-12 h-12 bg-blue-100 dark:bg-blue-900 rounded-full flex items-center justify-center">
          <User size={24} className="text-blue-600 dark:text-blue-300" />
        </div>
        <div>
          <h2 className="font-semibold text-gray-800 dark:text-white">Grace Arroyave</h2>
          <p className="text-sm text-gray-500 dark:text-gray-400">Nutricionista</p>
        </div>
      </div>

      {/* Menú Dashboard */}
      <div className="mb-8">
        <h3 className="text-xs font-semibold text-gray-400 dark:text-gray-500 uppercase mb-4">Dashboard</h3>
        <nav className="space-y-3">
          <a href="#" className="flex items-center gap-3 p-3 text-gray-700 dark:text-gray-300 rounded-xl bg-blue-50 dark:bg-gray-700">
            <Home size={20} className="text-blue-600 dark:text-blue-300" />
            <span className="text-base">Inicio</span>
          </a>
          <a href="#" className="flex items-center gap-3 p-3 text-gray-500 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-700 rounded-xl">
            <FileText size={20} />
            <span className="text-base">Planes</span>
          </a>
          <a href="#" className="flex items-center gap-3 p-3 text-gray-500 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-700 rounded-xl">
            <Users size={20} />
            <span className="text-base">Pacientes</span>
          </a>
        </nav>
      </div>

      {/* Menú Configuración */}
      <div>
        <h3 className="text-xs font-semibold text-gray-400 dark:text-gray-500 uppercase mb-4">Configuración</h3>
        <nav className="space-y-3">
          <a href="#" className="flex items-center gap-3 p-3 text-gray-500 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-700 rounded-xl">
            <Settings size={20} />
            <span className="text-base">Preferencias</span>
          </a>
          <a href="/logout" className="flex items-center gap-3 p-3 text-gray-500 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-700 rounded-xl">
            <LogOut size={20} />
            <span className="text-base">Cerrar Sesión</span>
          </a>
        </nav>
      </div>
    </aside>
  );
};

export default Sidebar;