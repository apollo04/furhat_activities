import { MantineProvider } from '@mantine/core';
import { RobotProvider } from 'contexts/RobotContext';
import { QueryClient, QueryClientProvider } from 'react-query';
import { ReactQueryDevtools } from 'react-query/devtools';
import { BrowserRouter } from 'react-router-dom';

import Router from './Router.tsx';
import theme from './styles/theme';

const App = () => {
  const queryClient = new QueryClient();

  return (
    <QueryClientProvider client={queryClient}>
      <MantineProvider theme={theme} withGlobalStyles withNormalizeCSS>
        <BrowserRouter>
          <RobotProvider>
            <Router />
          </RobotProvider>
        </BrowserRouter>
      </MantineProvider>

      <ReactQueryDevtools initialIsOpen={false} position='bottom-right' />
    </QueryClientProvider>
  );
};

export default App;
