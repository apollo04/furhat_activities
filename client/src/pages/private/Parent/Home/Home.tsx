import { Title, Stack, Text, Flex, Divider } from '@mantine/core';

const Home = () => {
  return (
    <Stack>
      <Flex direction='column'>
        <Title weight={700}>Dashboard</Title>
        <Text color='dimmed'>Your dashboard</Text>
      </Flex>

      <Divider my='md' />
    </Stack>
  );
};

export default Home;
