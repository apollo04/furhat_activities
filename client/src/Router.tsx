import React, { useEffect } from 'react';

import { Notifications } from '@mantine/notifications';
import ErrorBoundary from 'components/states/ErrorBoundary';

import Loading from './pages/shared/Loading.tsx';
import ServerError from './pages/shared/ServerError.tsx';
import PrivateLayout from './routes/layouts/PrivateLayout';

const Router = (): JSX.Element => {
  const loadAuthenticatedRouter = (): any => import('routes/PrivateRoutes');
  const PrivateRoutes = React.lazy(loadAuthenticatedRouter);

  useEffect(() => {
    loadAuthenticatedRouter();
  }, []);

  const Layout = (() => {
    return PrivateLayout;
  })();

  return (
    <ErrorBoundary errorMessage={<ServerError />}>
      <Notifications position='top-right' />
      <Layout>
        <React.Suspense fallback={<Loading />}>
          <PrivateRoutes />
        </React.Suspense>
      </Layout>
    </ErrorBoundary>
  );
};

export default Router;
