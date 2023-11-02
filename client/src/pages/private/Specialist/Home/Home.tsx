// import { useState } from 'react';

import { useEffect, useState } from 'react';

import {
  Title,
  Stack,
  Text,
  Flex,
  Divider,
  SimpleGrid,
  Badge,
  Group,
  Grid,
  Button,
  Select,
} from '@mantine/core';
import { useDisclosure } from '@mantine/hooks';
import { IconCheck, IconPlus, IconX } from '@tabler/icons-react';
import actionsData from 'mocks/actionData';
// import { Action } from 'types/generated';

import ActionCard from './components/ActionCard.tsx';
import DrawerFeedbackWriteForm from './components/DrawerFeedbackForm.tsx';

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
  const [seconds, setSeconds] = useState(0);
  const [isActive, setIsActive] = useState(false);

  const [
    isFeedbackFormOpened,
    { close: closeFeedbackForm, open: openFeedbackForm },
  ] = useDisclosure(false);

  useEffect(() => {
    let interval: any;

    if (isActive) {
      interval = setInterval(() => {
        setSeconds((prevSeconds) => prevSeconds + 1);
      }, 1000);
    } else if (!isActive && seconds !== 0) {
      clearInterval(interval);
    }

    return () => clearInterval(interval);
  }, [isActive, seconds]);

  const startTimer = () => {
    setIsActive(true);
  };

  const resetTimer = () => {
    setIsActive(false);
    setSeconds(0);
  };

  const formatTime = () => {
    const minutes = Math.floor(seconds / 60);
    const remainingSeconds = seconds % 60;
    const formattedTime = `${minutes
      .toString()
      .padStart(2, '0')}:${remainingSeconds.toString().padStart(2, '0')}`;
    return formattedTime;
  };

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

      <Grid columns={10}>
        <Grid.Col sm={10} md={10}>
          <Group position='left'>
            <Select data={['Алмаз Балгали']} placeholder='Select child' />
            {!isActive && (
              <Button leftIcon={<IconPlus />} onClick={() => startTimer()}>
                Start session
              </Button>
            )}
            {isActive && (
              <>
                <Button leftIcon={<IconX />} onClick={() => resetTimer()}>
                  Stop session
                </Button>
                <Button leftIcon={<IconCheck />} onClick={openFeedbackForm}>
                  Give feedback
                </Button>
                <Text>Timer: {formatTime()}</Text>
              </>
            )}
          </Group>
        </Grid.Col>
      </Grid>

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

      <DrawerFeedbackWriteForm
        opened={isFeedbackFormOpened}
        onClose={closeFeedbackForm}
        title='Give feedback'
      />
    </Stack>
  );
};

export default Home;
