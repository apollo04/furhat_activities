import { Button, Group, Modal, ModalProps, Text, Title } from '@mantine/core';
import useDeleteChild from 'hooks/children/useDeleteChild';
import { Child } from 'types/generated';
import {
  showErrorNotification,
  showSuccessNotification,
} from 'utils/notifications';

interface ModalDeleteChildProps extends Pick<ModalProps, 'opened' | 'onClose'> {
  child?: Child;
}

const ModalDeleteChild = ({
  opened,
  onClose,
  child,
}: ModalDeleteChildProps) => {
  const deleteChildMutation = useDeleteChild();

  const handleDelete = () => {
    if (child) {
      // eslint-disable-next-line no-underscore-dangle
      deleteChildMutation.mutate(child.id, {
        onSuccess: () => {
          showSuccessNotification('Ученик успешно удален');
          onClose();
        },
        onError: (error) => {
          showErrorNotification(
            'Ошибка при удалении ученика',
            error.response?.data.message || error.message,
          );
        },
      });
    }
  };

  return (
    <Modal
      opened={opened}
      onClose={onClose}
      title={<Title order={3}>Удалить ученика</Title>}
      centered
    >
      <Text>{`Вы точно хотите удалить "${child?.name}"? Изменения не подлежат восстановлению.`}</Text>
      <Group mt='md' position='right'>
        <Button
          variant='default'
          onClick={onClose}
          disabled={deleteChildMutation.isLoading}
        >
          Отмена
        </Button>
        <Button
          color='red'
          onClick={handleDelete}
          loading={deleteChildMutation.isLoading}
        >
          Удалить
        </Button>
      </Group>
    </Modal>
  );
};

export default ModalDeleteChild;
