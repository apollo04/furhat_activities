// import { useState } from 'react';

import { useEffect, useState } from 'react';

import {
  Title,
  Stack,
  Text,
  Flex,
  Divider,
  SimpleGrid,
  Group,
  Grid,
  Button,
  Avatar,
  Center,
  Loader,
} from '@mantine/core';
import { useForm } from '@mantine/form';
import { useDisclosure } from '@mantine/hooks';
import { IconCheck, IconFileAlert, IconPlus, IconX } from '@tabler/icons-react';
import ChildrenAutocomplete from 'components/auto-completes/ChildAutocomplete';
import EmptyState from 'components/states/EmptyState';
import useCategories from 'hooks/specialist/useCategories';
import actionsData from 'mocks/actionData';
import { DynamicAutoCompleteValue } from 'types/index';

import ActionCard from './components/ActionCard.tsx';
import DrawerConnectToRobot from './components/DrawerConnectToRobot.tsx';
import DrawerFeedbackWriteForm from './components/DrawerFeedbackForm.tsx';

interface FormValues {
  child: DynamicAutoCompleteValue;
}

const Home = () => {
  //   const [selectedAction, setSelectedAction] = useState<Action | undefined>(
  //     undefined,
  //   );
  const [seconds, setSeconds] = useState(0);
  const [isActive, setIsActive] = useState(false);

  const [categories, setCategories] = useState<any[]>([]);

  const { data, isSuccess, isLoading, isFetching, isError, error } =
    useCategories();

  const form = useForm<FormValues>({
    initialValues: {
      child: { value: '', label: '' },
    },
  });

  const [
    isFeedbackFormOpened,
    { close: closeFeedbackForm, open: openFeedbackForm },
  ] = useDisclosure(false);

  const [
    isConnectToRobotOpened,
    { close: closeConnectToRobot, open: openConnectToRobot },
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

  const handleCenterChange = (item: DynamicAutoCompleteValue | null) => {
    form.setFieldValue('child', {
      value: item?.value || '',
      label: item?.label || '',
    });
  };

  useEffect(() => {
    if (isSuccess && data?.data) {
      setCategories(data.data);
    }
  }, [isSuccess, data?.data]);

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
            <Button leftIcon={<IconPlus />} onClick={openConnectToRobot}>
              Connect to robot
            </Button>
            <ChildrenAutocomplete
              placeholder='Select child'
              value={form.values.child}
              onChange={handleCenterChange}
            />
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

      {isLoading && isFetching && (
        <Center mt='xl'>
          <Loader />
        </Center>
      )}

      {isSuccess && categories.length === 0 && (
        <EmptyState
          title='No Categories'
          description='There are no Categories to display.'
        />
      )}

      {isError && (
        <EmptyState
          mt='xl'
          title='Error'
          description={
            error?.response?.data.message ||
            'Something went wrong while fetching data.'
          }
          Icon={
            <Avatar radius='100%' size='xl' variant='light' color='red'>
              <IconFileAlert size={25} />
            </Avatar>
          }
        />
      )}

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
          <ActionCard key={action.name} img={action.image} name={action.name} />
        ))}
      </SimpleGrid>

      <DrawerFeedbackWriteForm
        opened={isFeedbackFormOpened}
        onClose={closeFeedbackForm}
        title='Give feedback'
      />

      <DrawerConnectToRobot
        opened={isConnectToRobotOpened}
        onClose={closeConnectToRobot}
        title='Connect to robot'
      />
    </Stack>
  );
};

export default Home;
