import { matchRoutes, useLocation } from 'react-router-dom';
import { publicRoutesMap } from 'routes/PublicRoutes';
import { SpecialistRoutesMap } from 'routes/roles/Specialist';

export default function useCurrentRoute(): string {
  const routes = ['/'].concat(
    Object.keys(publicRoutesMap),
    Object.keys(SpecialistRoutesMap),
  );

  const location = useLocation();
  const uniqRoutes = [...new Set(routes)];
  const matchedRoutes = matchRoutes(
    uniqRoutes.map((item) => ({ path: item })),
    location,
  );

  if (Array.isArray(matchedRoutes)) {
    return matchedRoutes[0].route.path;
  }

  return '';
}
