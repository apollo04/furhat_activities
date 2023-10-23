import Home from 'pages/private/Specialist/Home';
import NotFound from 'pages/shared/NotFound';
import { Navigate, Route, Routes } from 'react-router-dom';
import { RoutesMap } from 'routes/types';

export const SpecialistRoutesMap: RoutesMap = {
  '/login': <Navigate to='/' replace />,
  '/register': <Navigate to='/' replace />,
  '*': <NotFound />,
  '/': <Home />,
};

const Specialist = () => {
  return (
    <Routes>
      {Object.keys(SpecialistRoutesMap).map((path) => (
        <Route key={path} path={path} element={SpecialistRoutesMap[path]} />
      ))}
    </Routes>
  );
};

export default Specialist;
