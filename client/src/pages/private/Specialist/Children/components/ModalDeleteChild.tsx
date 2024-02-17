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
          showSuccessNotification('Child delete success');
          onClose();
        },
        onError: (error) => {
          showErrorNotification(
            'Child delete failed',
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
      title={<Title order={3}>Delete Child</Title>}
      centered
    >
      <Text>{`Are you sure that you want to delete "${child?.name}"? The changes are not recoverable.`}</Text>
      <Group mt='md' position='right'>
        <Button
          variant='default'
          onClick={onClose}
          disabled={deleteChildMutation.isLoading}
        >
          Cancel
        </Button>
        <Button
          color='red'
          onClick={handleDelete}
          loading={deleteChildMutation.isLoading}
        >
          Delete
        </Button>
      </Group>
    </Modal>
  );
};

export default ModalDeleteChild;
