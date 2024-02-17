import {
  Button,
  Drawer,
  DrawerProps,
  Group,
  NumberInput,
  Select,
  Stack,
  TextInput,
  Title,
} from '@mantine/core';
import { useForm } from '@mantine/form';
import useCreateChild from 'hooks/children/useCreateChild';
import {
  showErrorNotification,
  showSuccessNotification,
} from 'utils/notifications';

interface FormValues {
  name: string;
  surname: string;
  age: string;
  gender: string;
}

interface DrawerFarmWriteFromProps
  extends Pick<DrawerProps, 'opened' | 'onClose'> {
  title: string;
}

const DrawerChildWriteForm = ({
  opened,
  onClose,
  title,
}: DrawerFarmWriteFromProps) => {
  const createChildMutation = useCreateChild();

  const nextWeekDate = new Date();
  nextWeekDate.setDate(nextWeekDate.getDate() + 7);

  const initialValues = {
    name: '',
    surname: '',
    age: '',
    gender: '',
  };

  const form = useForm<FormValues>({
    initialValues,
  });

  const actionButtonsDisabled = createChildMutation.isLoading;

  const handleResetAndClose = () => {
    form.reset();
    onClose();
  };

  const handleSubmit = (formValues: FormValues) => {
    const createPayload = {
      ...formValues,
    };

    createChildMutation.mutate(createPayload, {
      onSuccess: () => {
        showSuccessNotification('Child creation is success');
        form.reset();
        onClose();
      },
      onError: (error) => {
        showErrorNotification(
          'Child creation failed',
          error.response?.data.message || error.message,
        );
      },
    });
  };

  return (
    <Drawer
      opened={opened}
      onClose={handleResetAndClose}
      title={<Title order={3}>{title}</Title>}
      sx={{ position: 'relative' }}
    >
      <form onSubmit={form.onSubmit(handleSubmit)}>
        <Stack spacing='xs'>
          <TextInput
            label='Name'
            placeholder='Name'
            {...form.getInputProps('name')}
            required
          />
          <TextInput
            label='Surname'
            placeholder='Surname'
            {...form.getInputProps('surname')}
            required
          />
          <NumberInput
            label='Age'
            placeholder='Age'
            min={0}
            required
            {...form.getInputProps('age')}
          />
          <Select
            label='Gender'
            data={['male', 'female', 'other']}
            placeholder='Gender'
            {...form.getInputProps('gender')}
            required
          />
        </Stack>

        <Group position='right' mt='lg'>
          <Button
            variant='subtle'
            onClick={handleResetAndClose}
            disabled={actionButtonsDisabled}
          >
            Cancel
          </Button>
          <Button type='submit' loading={actionButtonsDisabled}>
            Create
          </Button>
        </Group>
      </form>
    </Drawer>
  );
};

export default DrawerChildWriteForm;
