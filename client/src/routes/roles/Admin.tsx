import Home from 'pages/private/Admin/Home';
import NotFound from 'pages/shared/NotFound';
import { Navigate, Route, Routes } from 'react-router-dom';
import { RoutesMap } from 'routes/types';

export const AdminRoutesMap: RoutesMap = {
  '/login': <Navigate to='/' replace />,
  '/register': <Navigate to='/' replace />,
  '*': <NotFound />,
  '/': <Home />,
};

const Admin = () => {
  return (
    <Routes>
      {Object.keys(AdminRoutesMap).map((path) => (
        <Route key={path} path={path} element={AdminRoutesMap[path]} />
      ))}
    </Routes>
  );
};

export default Admin;
