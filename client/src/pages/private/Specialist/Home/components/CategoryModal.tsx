import { useEffect, useState } from 'react';

import {
  Center,
  Loader,
  Avatar,
  SegmentedControl,
  Grid,
  Modal,
  Button,
  Flex,
} from '@mantine/core';
import { IconFileAlert, IconHandStop } from '@tabler/icons-react';
import EmptyState from 'components/states/EmptyState';
import useStopFurhat from 'hooks/furhat/useStopFurhat';
import useActions from 'hooks/specialist/useActions';
import {
  showErrorNotification,
  showSuccessNotification,
} from 'utils/notifications';

import ActionCard from './ActionCard.tsx';

interface CategoryModalProps {
  opened: boolean;
  onClose: () => void;
  size: 'xs' | 'sm' | 'md' | 'lg' | 'xl';
  category: string;
  robotInfo?: {
    ip: string;
    name: string;
  };
}

const CategoryModal = ({
  opened,
  onClose,
  size,
  category,
  robotInfo,
}: CategoryModalProps): JSX.Element => {
  const stopFurhatMutation = useStopFurhat(robotInfo!.ip);
  const [language, setLanguage] = useState('kk');
  const [actions, setActions] = useState<any[]>([]);
  const [categoryData, setCategoryData] = useState<any>({});

  useEffect(() => {
    if (language === 'kk' && categoryData?.actions_kaz) {
      setActions(categoryData?.actions_kaz);
    } else if (language === 'ru' && categoryData?.actions_rus) {
      setActions(categoryData?.actions_rus);
    }
  }, [language, categoryData]);

  const { data, isSuccess, isLoading, isFetching, isError, error } =
    useActions(category);

  useEffect(() => {
    if (isSuccess && data?.data && opened) {
      setCategoryData(data.data);
    }
  }, [isSuccess, data?.data, opened]);

  const handleStopFurhat = () => {
    stopFurhatMutation.mutate(null, {
      onSuccess: () => {
        showSuccessNotification('Робот успешно остановлен');
      },
      onError: (robot_error) => {
        showErrorNotification(
          'Ошибка при остановке робота',
          robot_error.response?.data.message || robot_error.message,
        );
      },
    });
  };

  return (
    <>
      {isLoading && isFetching && (
        <Center mt='xl'>
          <Loader />
        </Center>
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
      <Modal
        opened={opened}
        onClose={onClose}
        title='Начать упражнение'
        size={size}
      >
        <Flex direction='column'>
          <SegmentedControl
            value={language}
            onChange={setLanguage}
            data={[
              { label: 'Қазақша', value: 'kk' },
              { label: 'Русский', value: 'ru' },
            ]}
          />

          <Flex justify='space-between' align='center'>
            <p style={{ fontSize: '24px', fontWeight: '600' }}>
              {category.charAt(0).toUpperCase() + category.slice(1)}
            </p>

            <Button
              leftIcon={<IconHandStop />}
              onClick={handleStopFurhat}
              disabled={stopFurhatMutation.isLoading}
              color='red'
            >
              Экстренный Стоп
            </Button>
          </Flex>

          <Grid
            style={{
              gap: '1.5rem',
              paddingTop: '1rem',
              paddingBottom: '2rem',
              paddingRight: '1rem',
              paddingLeft: '1rem',
            }}
          >
            {actions.map((action) => (
              <ActionCard
                key={action.id}
                category={category}
                robotInfo={robotInfo}
                action={action}
              />
            ))}
          </Grid>
        </Flex>
      </Modal>
    </>
  );
};

export default CategoryModal;
