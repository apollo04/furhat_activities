import { Alert, Center, Text, Title } from '@mantine/core';
import { useAuth } from 'contexts/AuthContext';

import Admin from './roles/Admin.tsx';
import Parent from './roles/Parent.tsx';
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
  if (profile.role === 'parent') {
    return <Parent />;
  }
  if (profile.role === 'admin') {
    return <Admin />;
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
