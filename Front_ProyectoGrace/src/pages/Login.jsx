import React from 'react';
import { useForm } from 'react-hook-form';
import { toast } from 'react-hot-toast';
import { useNavigate } from 'react-router-dom';
import { login } from '../api/auth';

const Login = () => {
  const { register, handleSubmit } = useForm();
  const navigate = useNavigate();

  const onSubmit = async (data) => {
    try {
      const { access, refresh } = await login(data.email, data.password);
      localStorage.setItem('accessToken', access);
      localStorage.setItem('refreshToken', refresh);
      toast.success('Inicio de sesión exitoso');
      navigate('/dashboard');
    } catch (error) {
      toast.error(error.message);
    }
  };

  return (
    <div>
      <h2>Login</h2>
      <form onSubmit={handleSubmit(onSubmit)}>
        <div>
          <label>Email</label>
          <input type="email" {...register('email', { required: true })} />
        </div>
        <div>
          <label>Password</label>
          <input type="password" {...register('password', { required: true })} />
        </div>
        <button type="submit">Iniciar Sesión</button>
      </form>
      
    </div>
  );
};

export default Login;
