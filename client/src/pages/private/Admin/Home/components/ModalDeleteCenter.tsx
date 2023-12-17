import { Button, Group, Modal, ModalProps, Text, Title } from '@mantine/core';
import useDeleteCenter from 'hooks/center/useDeleteCenter';
import { Center } from 'types/generated';
import {
  showErrorNotification,
  showSuccessNotification,
} from 'utils/notifications';

interface ModalDeleteCenterProps
  extends Pick<ModalProps, 'opened' | 'onClose'> {
  center?: Center;
}

const ModalDeleteCenter = ({
  opened,
  onClose,
  center,
}: ModalDeleteCenterProps): JSX.Element => {
  const deleteCenterMutation = useDeleteCenter();

  const handleDelete = async () => {
    if (center) {
      // eslint-disable-next-line no-underscore-dangle
      deleteCenterMutation.mutate(center._id, {
        onSuccess: () => {
          showSuccessNotification('Center deleted successfully');
          onClose();
        },
        onError: (error) => {
          showErrorNotification(
            'Center cancel failed',
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
      title={<Title order={3}>Cancel Center</Title>}
      centered
    >
      <Text>Are you sure you want to cancel Center?</Text>
      <Group mt='md' position='right'>
        <Button variant='default' onClick={onClose}>
          Cancel
        </Button>
        <Button color='red' onClick={handleDelete}>
          Delete
        </Button>
      </Group>
    </Modal>
  );
};

export default ModalDeleteCenter;
