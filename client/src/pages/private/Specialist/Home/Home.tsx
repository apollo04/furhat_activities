// import { useState } from 'react';

import { useState } from 'react';

import {
  Title,
  Stack,
  Text,
  Flex,
  Divider,
  SimpleGrid,
  Badge,
  Group,
} from '@mantine/core';
import actionsData from 'mocks/actionData';
// import { Action } from 'types/generated';

import ActionCard from './components/ActionCard.tsx';

const FILTERS = [
  'all',
  'social',
  'receptive',
  'sensory',
  'expressive lang.',
  'cognitive',
  'phys. ed.',
];

const Home = () => {
  //   const [selectedAction, setSelectedAction] = useState<Action | undefined>(
  //     undefined,
  //   );
  const [filters, setFilters] = useState<string[]>([]);

  const handleFilters = (filter: string) => {
    if (filters.includes(filter)) {
      setFilters((prev) => prev.filter((item) => item !== filter));
    } else {
      setFilters((prev) => [...prev, filter]);
    }
  };

  return (
    <Stack>
      <Flex direction='column'>
        <Title weight={700}>Actions</Title>
        <Text color='dimmed'>Select robot action</Text>
      </Flex>

      <Divider my='md' />

      <Group spacing='sm'>
        {FILTERS.map((filter) => (
          <Badge
            key={filter}
            onClick={() => handleFilters(filter)}
            variant={filters.includes(filter) ? 'default' : 'outline'}
          >
            {filter}
          </Badge>
        ))}
      </Group>

      <SimpleGrid
        mt='xl'
        spacing='lg'
        breakpoints={[
          { minWidth: 'sm', cols: 2 },
          { minWidth: 'md', cols: 3 },
          { minWidth: 'lg', cols: 4 },
        ]}
        sx={{ position: 'relative' }}
      >
        {actionsData.map((action) => (
          <ActionCard
            key={action.name}
            img={action.image}
            name={action.name}
            badges={action.badges}
          />
        ))}
      </SimpleGrid>
    </Stack>
  );
};

export default Home;
