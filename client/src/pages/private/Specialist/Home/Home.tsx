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
import { DynamicAutoCompleteValue } from 'types/index';

import CategoryCard from './components/CategoryCard.tsx';
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
  const [robotInfo, setRobotInfo] = useState({
    ip: '',
    name: '',
  });
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
    openFeedbackForm();
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

  const handleChildChange = (item: DynamicAutoCompleteValue | null) => {
    form.setFieldValue('child', {
      value: item?.value || '',
      label: item?.label || '',
    });
  };

  // eslint-disable-next-line @typescript-eslint/no-shadow
  const handleRobotInfoChange = (robotInfo: { ip: string; name: string }) => {
    setRobotInfo(robotInfo);
  };

  useEffect(() => {
    if (isSuccess && data?.data) {
      setCategories(data.data);
    }
  }, [isSuccess, data?.data]);

  return (
    <Stack>
      <Flex direction='column'>
        <Title weight={700}>Категории</Title>
        <Text color='dimmed'>Выберите категорию</Text>
      </Flex>

      <Divider my='md' />

      <Grid columns={10}>
        <Grid.Col sm={10} md={10}>
          <Group position='left'>
            <Button leftIcon={<IconPlus />} onClick={openConnectToRobot}>
              Подключитесь к роботу
            </Button>

            {robotInfo.ip && (
              <>
                <ChildrenAutocomplete
                  placeholder='Выберите ученика'
                  value={form.values.child}
                  onChange={handleChildChange}
                />
                {!isActive && (
                  <Button leftIcon={<IconPlus />} onClick={() => startTimer()}>
                    Начать сессию
                  </Button>
                )}
                {isActive && (
                  <>
                    <Button leftIcon={<IconX />} onClick={() => resetTimer()}>
                      Завершить сессию
                    </Button>
                    <Button leftIcon={<IconCheck />} onClick={openFeedbackForm}>
                      Оставить отзыв
                    </Button>
                    <Text>Таймер: {formatTime()}</Text>
                  </>
                )}
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
          title='Не найдено категории'
          description='Нет категории для отображения.'
        />
      )}

      {isError && (
        <EmptyState
          mt='xl'
          title='Error'
          description={
            error?.response?.data.message ||
            'Что то пошло не так, попробуйте позже.'
          }
          Icon={
            <Avatar radius='100%' size='xl' variant='light' color='red'>
              <IconFileAlert size={25} />
            </Avatar>
          }
        />
      )}

      {isActive && (
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
          {categories.map((action) => (
            <CategoryCard
              key={action.name}
              imgSrc={action.icon}
              name={action.category}
              robotInfo={robotInfo}
            />
          ))}
        </SimpleGrid>
      )}

      <DrawerFeedbackWriteForm
        childId={form.values.child.value}
        opened={isFeedbackFormOpened}
        onClose={closeFeedbackForm}
        title='Оставить отзыв'
      />

      <DrawerConnectToRobot
        handleSetRobotInfo={handleRobotInfoChange}
        opened={isConnectToRobotOpened}
        onClose={closeConnectToRobot}
        title='Подключитесь к роботу'
      />
    </Stack>
  );
};

export default Home;
