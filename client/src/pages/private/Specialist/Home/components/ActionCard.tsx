import { Paper, Group, Image, Stack, Title } from "@mantine/core";
// import useAction from 'hooks/specialist/useAction';

interface ActionCardProps {
    robotInfo: any;
    action: any
}

export const ActionCard = ({ action, robotInfo }: ActionCardProps): JSX.Element => {
    // const handleStartAction = () => {
    //     const { data, isSuccess, isLoading, isError, error } = useAction(action.category, action.action, "5353353");
    //     console.log(data);
    //     if (isSuccess) {
    //         console.log("success");
    //     }
    // 
    return (
        <>
    <Paper onClick={() => {}} shadow='md' className='categoryCard' style={{cursor: "pointer"}} sx={{ position: 'relative', overflow: 'hidden' }} >
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
      <Image src={`images/actions/holidays.png`} width='100%' height={160} alt={action.action} />
      <Stack pt='xs' pb='sm' px='md' spacing='xs'>
        <Title order={5} weight={700}>
          {action.action.charAt(0).toUpperCase() + action.action.slice(1)}
        </Title>
      </Stack>
    </Paper>
    </>
    );
}