import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { Toaster } from 'react-hot-toast'; // Cambio de ToastContainer a Toaster
import ProtectedRoute from './components/ProtectedRoute';
import Dashboard from './pages/Dashboard';
import Login from './pages/Login';
import LogoutPage from './pages/LogoutPage';

function App() {
  return (
    <BrowserRouter>
      <Toaster // Componente actualizado
        position="top-right"
        toastOptions={{
          className: '!bg-white !text-gray-800 dark:!bg-gray-700 dark:!text-gray-100',
          duration: 3000
        }}
      />
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/login" element={<Login />} />
        <Route
          path="/dashboard"
          element={
            <ProtectedRoute>
              <Dashboard />
            </ProtectedRoute>
          }
        />
        <Route path="/logout" element={<LogoutPage />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;