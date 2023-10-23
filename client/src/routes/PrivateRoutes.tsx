import { Alert, Center, Text, Title } from '@mantine/core';
import { useAuth } from 'contexts/AuthContext';

import Specialist from './roles/Specialist.tsx';

const PrivateRoutes = (): JSX.Element => {
  const {
    profile,
  }: {
    profile: any;
  } = useAuth();

  if (profile.role === 'specialist') {
    return <Specialist />;
  }

  return (
    <Center>
      <Alert color='red' title={<Title order={3}>Error</Title>}>
        <Text>Unauthorized access.</Text>
      </Alert>
    </Center>
  );
};

export default PrivateRoutes;
