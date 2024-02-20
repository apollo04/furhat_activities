import { Paper, Group, Image, Stack, Title } from '@mantine/core';
import useAction from 'hooks/specialist/useAction';
import {
  showSuccessNotification,
  showErrorNotification,
} from 'utils/notifications';

interface ActionCardProps {
  category: string;
  robotInfo: any;
  action: any;
}

const ActionCard = ({
  category,
  action,
  robotInfo,
}: ActionCardProps): JSX.Element => {
  const actionMutation = useAction(category, action.id, robotInfo.ip);

  const handleClick = () => {
    if (category && action && robotInfo) {
      actionMutation.mutate(null, {
        onSuccess: () => {
          showSuccessNotification('Action success');
        },
        onError: (error) => {
          showErrorNotification(
            'Action failed',
            error.response?.data.message || error.message,
          );
        },
      });
    }
  };

  return (
    <Paper
      onClick={handleClick}
      shadow='md'
      className='categoryCard'
      style={{ cursor: 'pointer' }}
      sx={{ position: 'relative', overflow: 'hidden' }}
    >
      <Group
        position='right'
        pt='xs'
        px='xs'
        sx={{
          position: 'absolute',
          left: 0,
          top: 0,
          right: 0,
          zIndex: 10,
        }}
      ></Group>
      <Image
        src={`data:image/png;base64,${action.icon}`}
        width='100%'
        height={160}
        alt={action.action}
      />
      <Stack pt='xs' pb='sm' px='md' spacing='xs'>
        <Title order={5} weight={700}>
          {action.action.charAt(0).toUpperCase() + action.action.slice(1)}
        </Title>
      </Stack>
    </Paper>
  );
};

export default ActionCard;
