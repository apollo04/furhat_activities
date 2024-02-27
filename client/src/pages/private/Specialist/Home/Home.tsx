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
  Box,
} from '@mantine/core';
import { useForm } from '@mantine/form';
import { useDisclosure } from '@mantine/hooks';
import { IconCheck, IconFileAlert, IconPlus, IconX } from '@tabler/icons-react';
import ChildrenAutocomplete from 'components/auto-completes/ChildAutocomplete';
import EmptyState from 'components/states/EmptyState';
import { useRobot } from 'contexts/RobotContext';
import useCategories from 'hooks/specialist/useCategories';
import { DynamicAutoCompleteValue } from 'types/index';

import CategoryCard from './components/CategoryCard.tsx';
import DrawerFeedbackWriteForm from './components/DrawerFeedbackForm.tsx';

interface FormValues {
  child: DynamicAutoCompleteValue;
}

const Home = () => {
  const { robotInfo } = useRobot();
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

  useEffect(() => {
    if (isSuccess && data?.data) {
      setCategories(data.data);
    }
  }, [isSuccess, data?.data]);

  return (
    <Stack pos='relative'>
      <Flex direction='column'>
        <Title weight={700}>Категории</Title>
        <Text color='dimmed'>Выберите категорию</Text>
      </Flex>

      <Divider my='md' />

      <Grid columns={10}>
        <Grid.Col sm={10} md={10}>
          <Group position='left'>
            <ChildrenAutocomplete
              placeholder='Выберите ученика'
              value={form.values.child}
              onChange={handleChildChange}
              disabled={!robotInfo?.ip || isActive}
            />
            {!isActive && (
              <Button
                disabled={!robotInfo?.ip || !form.values.child.value}
                leftIcon={<IconPlus />}
                onClick={() => startTimer()}
              >
                Начать сессию
              </Button>
            )}
            {isActive && (
              <>
                <Button
                  color='red'
                  leftIcon={<IconX />}
                  onClick={() => resetTimer()}
                >
                  Завершить сессию
                </Button>
                <Button leftIcon={<IconCheck />} onClick={openFeedbackForm}>
                  Оценить
                </Button>
                <Text>Таймер: {formatTime()}</Text>
              </>
            )}
          </Group>
        </Grid.Col>
      </Grid>
      <Box sx={{ position: 'relative' }}>
        {(!robotInfo?.ip || !isActive) && (
          <Box
            sx={{
              position: 'absolute',
              top: 0,
              left: '-2.5%',
              width: '105%',
              height: '100%',
              backgroundColor: 'rgba(128, 128, 128, 0.5)',
              zIndex: 2,
            }}
          />
        )}

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

        <SimpleGrid
          mt='xl'
          spacing='lg'
          breakpoints={[
            { minWidth: 'sm', cols: 2 },
            { minWidth: 'md', cols: 3 },
            { minWidth: 'lg', cols: 4 },
          ]}
          sx={{ position: 'relative', zIndex: 1 }}
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
      </Box>

      {categories && (
        <DrawerFeedbackWriteForm
          categories={categories}
          childId={form.values.child.value}
          isActive={isActive}
          opened={isFeedbackFormOpened}
          onClose={closeFeedbackForm}
          title='Оставить оценку'
        />
      )}
    </Stack>
  );
};

export default Home;
