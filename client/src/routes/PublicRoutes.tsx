import LoginParent from 'pages/public/LoginParent';
import LoginRoleSelect from 'pages/public/LoginRoleSelect';
import LoginSpecialist from 'pages/public/LoginSpecialist';
import RegisterParent from 'pages/public/RegisterParent/RegisterParent';
import RegisterSpecialist from 'pages/public/RegisterSpecialist/RegisterSpecialist';
import { Navigate, Route, Routes } from 'react-router-dom';

import { RoutesMap } from './types';

export const publicRoutesMap: RoutesMap = {
  '/login': <LoginRoleSelect />,
  '/login/specialist': <LoginSpecialist />,
  '/login/parent': <LoginParent />,
  '/register/specialist': <RegisterParent />,
  '/register/parent': <RegisterSpecialist />,
  '*': <Navigate to='/login' />,
};

const PublicRoutes = (): JSX.Element => {
  return (
    <Routes>
      {Object.keys(publicRoutesMap).map((path) => (
        <Route key={path} path={path} element={publicRoutesMap[path]} />
      ))}
    </Routes>
  );
};

export default PublicRoutes;
