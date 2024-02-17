import {
  Button,
  Drawer,
  DrawerProps,
  Group,
  Title,
  TextInput,
  Select,
  Stack,
} from '@mantine/core';
import { useForm } from '@mantine/form';

interface FormValues {
  ip: string;
  name: string;
}

interface DrawerConnectToRobotProps
  extends Pick<DrawerProps, 'opened' | 'onClose'> {
  title: string;
}

const DrawerConnectToRobot = ({
  opened,
  onClose,
  title,
}: DrawerConnectToRobotProps) => {
  const form = useForm<FormValues>({
    initialValues: {
      ip: '',
      name: '',
    },
  });

  const handleResetAndClose = () => {
    form.reset();
    onClose();
  };

  const handleSubmit = () => {
    // const robotName = formValues.name;
    // const robotIp = formValues.ip;
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
          <Select
            label='Robot'
            data={['NAO', 'MIRAI', 'FURHAT']}
            {...form.getInputProps('name')}
            required
          />
          <TextInput label='Robot ip' {...form.getInputProps('ip')} required />
        </Stack>

        <Group position='right' mt='xl'>
          <Button variant='subtle' onClick={handleResetAndClose}>
            Cancel
          </Button>
          <Button type='submit'>Connect</Button>
        </Group>
      </form>
    </Drawer>
  );
};

export default DrawerConnectToRobot;
