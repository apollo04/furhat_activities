import Home from 'pages/private/Parent/Home';
import NotFound from 'pages/shared/NotFound';
import { Navigate, Route, Routes } from 'react-router-dom';
import { RoutesMap } from 'routes/types';

export const ParentRoutesMap: RoutesMap = {
  '/login': <Navigate to='/' replace />,
  '/register': <Navigate to='/' replace />,
  '*': <NotFound />,
  '/': <Home />,
};

const Parent = () => {
  return (
    <Routes>
      {Object.keys(ParentRoutesMap).map((path) => (
        <Route key={path} path={path} element={ParentRoutesMap[path]} />
      ))}
    </Routes>
  );
};

export default Parent;
