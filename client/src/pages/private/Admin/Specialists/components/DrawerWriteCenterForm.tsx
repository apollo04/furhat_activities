import {
  Button,
  Drawer,
  DrawerProps,
  Group,
  Stack,
  TextInput,
  Title,
} from '@mantine/core';
import { useForm } from '@mantine/form';
import { useShallowEffect } from '@mantine/hooks';
import useCreateCenter from 'hooks/center/useCreateCenter';
import useUpdateCenter from 'hooks/center/useUpdateCenter';
import { Center } from 'types/generated';
import {
  showErrorNotification,
  showSuccessNotification,
} from 'utils/notifications';

interface FormValues {
  name: string;
  country: string;
  city: string;
  street: string;
}

interface DrawerCenterWriteFromProps
  extends Pick<DrawerProps, 'opened' | 'onClose'> {
  center?: Center;
  title: string;
}

const DrawerCenterWriteFrom = ({
  center,
  opened,
  onClose,
  title,
}: DrawerCenterWriteFromProps) => {
  const createCenterMutation = useCreateCenter();
  // eslint-disable-next-line no-underscore-dangle
  const updateCenterMutation = useUpdateCenter(center && center._id);

  const form = useForm<FormValues>({
    initialValues: {
      name: '',
      country: '',
      city: '',
      street: '',
    },
  });

  const handleResetAndClose = () => {
    form.reset();
    onClose();
  };

  const handleSubmit = (formValues: FormValues) => {
    if (center) {
      const updatePayload = {
        ...formValues,
        // eslint-disable-next-line no-underscore-dangle
        id: center._id,
      };

      updateCenterMutation.mutate(updatePayload, {
        onSuccess: () => {
          showSuccessNotification('Center update is success');
          handleResetAndClose();
        },
        onError: (error) => {
          showErrorNotification(
            'Center update failed',
            error.response?.data.message || error.message,
          );
        },
      });
    } else {
      const createPayload = {
        ...formValues,
      };

      createCenterMutation.mutate(createPayload, {
        onSuccess: () => {
          showSuccessNotification('Center creation is success');
          handleResetAndClose();
        },
        onError: (error) => {
          showErrorNotification(
            'Center creation failed',
            error.response?.data.message || error.message,
          );
        },
      });
    }
  };

  useShallowEffect(() => {
    if (center) {
      form.setFieldValue('name', center.name);
      form.setFieldValue('country', center.country);
      form.setFieldValue('city', center.city);
      form.setFieldValue('street', center.street);
    }
  }, [center]);

  return (
    <Drawer
      opened={opened}
      onClose={handleResetAndClose}
      title={<Title order={3}>{title}</Title>}
    >
      <form onSubmit={form.onSubmit(handleSubmit)}>
        <Stack spacing='xs'>
          <TextInput label='Name' {...form.getInputProps('name')} required />
          <TextInput
            label='Country'
            {...form.getInputProps('country')}
            required
          />
          <TextInput label='City' {...form.getInputProps('city')} required />
          <TextInput
            label='Street'
            {...form.getInputProps('street')}
            required
          />

          <Group position='right' mt='xl'>
            <Button
              variant='subtle'
              onClick={handleResetAndClose}
              disabled={
                createCenterMutation.isLoading || updateCenterMutation.isLoading
              }
            >
              Cancel
            </Button>
            <Button
              type='submit'
              loading={
                createCenterMutation.isLoading || updateCenterMutation.isLoading
              }
            >
              {center ? 'Update' : 'Create'}
            </Button>
          </Group>
        </Stack>
      </form>
    </Drawer>
  );
};

export default DrawerCenterWriteFrom;
