import { Group, Image, Paper, Stack, Title } from '@mantine/core';

interface ActionCardProps {
  img: string;
  name: string;
}

const ActionCard = ({ img, name }: ActionCardProps) => {
  return (
    <Paper shadow='md' sx={{ position: 'relative', overflow: 'hidden' }}>
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
      <Image src={img} width='100%' height={160} alt={name} />

      <Stack pt='xs' pb='sm' px='md' spacing='xs'>
        <Title order={5} weight={700}>
          {name}
        </Title>
      </Stack>
    </Paper>
  );
};

export default ActionCard;
