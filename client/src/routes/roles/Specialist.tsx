import Home from "pages/private/Specialist/Home";
import Students from "pages/private/Specialist/Children";
import NotFound from "pages/shared/NotFound";
import { Navigate, Route, Routes } from "react-router-dom";
import { RoutesMap } from "routes/types";
import Settings from "pages/private/Specialist/Settings";

export const SpecialistRoutesMap: RoutesMap = {
  "/login": <Navigate to="/" replace />,
  "/register": <Navigate to="/" replace />,
  "*": <NotFound />,
  "/": <Home />,
  "/students": <Students />,
  "/settings": <Settings />,
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
