import {
  Button,
  Drawer,
  DrawerProps,
  Group,
  Slider,
  Stack,
  Title,
  Text,
} from '@mantine/core';
import { useForm } from '@mantine/form';

interface FormValues {
  grades: string[];
}

interface DrawerFeedbackFormProps
  extends Pick<DrawerProps, 'opened' | 'onClose'> {
  title: string;
}

const DrawerFeedbackForm = ({
  opened,
  onClose,
  title,
}: DrawerFeedbackFormProps) => {
  const form = useForm<FormValues>();

  const handleResetAndClose = () => {
    form.reset();
    onClose();
  };

  const handleSubmit = () => {};

  return (
    <Drawer
      opened={opened}
      onClose={handleResetAndClose}
      title={<Title order={3}>{title}</Title>}
      sx={{ position: 'relative' }}
    >
      <form onSubmit={form.onSubmit(handleSubmit)}>
        <Stack spacing='xl'>
          <Stack spacing='xs'>
            <Text>A</Text>
            <Slider
              color='blue'
              label='A'
              step={10}
              marks={[
                { value: 0, label: '0' },
                { value: 10, label: '1' },
                { value: 20, label: '2' },
                { value: 30, label: '3' },
                { value: 40, label: '4' },
                { value: 50, label: '5' },
                { value: 60, label: '6' },
                { value: 70, label: '7' },
                { value: 80, label: '8' },
                { value: 90, label: '9' },
                { value: 100, label: '10' },
              ]}
            />
          </Stack>

          <Stack spacing='xs'>
            <Text>B</Text>
            <Slider
              color='blue'
              step={10}
              marks={[
                { value: 0, label: '0' },
                { value: 10, label: '1' },
                { value: 20, label: '2' },
                { value: 30, label: '3' },
                { value: 40, label: '4' },
                { value: 50, label: '5' },
                { value: 60, label: '6' },
                { value: 70, label: '7' },
                { value: 80, label: '8' },
                { value: 90, label: '9' },
                { value: 100, label: '10' },
              ]}
            />
          </Stack>

          <Stack spacing='xs'>
            <Text>C</Text>
            <Slider
              color='blue'
              step={10}
              marks={[
                { value: 0, label: '0' },
                { value: 10, label: '1' },
                { value: 20, label: '2' },
                { value: 30, label: '3' },
                { value: 40, label: '4' },
                { value: 50, label: '5' },
                { value: 60, label: '6' },
                { value: 70, label: '7' },
                { value: 80, label: '8' },
                { value: 90, label: '9' },
                { value: 100, label: '10' },
              ]}
            />
          </Stack>
        </Stack>

        <Group position='right' mt='xl'>
          <Button variant='subtle' onClick={handleResetAndClose}>
            Cancel
          </Button>
          <Button type='submit'>Submit</Button>
        </Group>
      </form>
    </Drawer>
  );
};

export default DrawerFeedbackForm;
