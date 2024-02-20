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
import { useRobot } from 'contexts/RobotContext';

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
  const { handleSetRobotInfo } = useRobot();

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

  const handleSubmit = (formValues: FormValues) => {
    const robotName = formValues.name;
    const robotIp = formValues.ip;
    handleSetRobotInfo({ ip: robotIp, name: robotName });
    onClose();
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
            label='Робот'
            data={['NAO', 'MIRAI']}
            {...form.getInputProps('name')}
            required
          />
          <TextInput label='IP робота' {...form.getInputProps('ip')} required />
        </Stack>

        <Group position='right' mt='xl'>
          <Button variant='subtle' onClick={handleResetAndClose}>
            Отмена
          </Button>
          <Button type='submit'>Подлючиться</Button>
        </Group>
      </form>
    </Drawer>
  );
};

export default DrawerConnectToRobot;
