import { useEffect, useState } from 'react';

import {
  Title,
  Stack,
  Text,
  Flex,
  Divider,
  Grid,
  TextInput,
  Paper,
  Avatar,
  useMantineTheme,
  Group,
  Button,
  ActionIcon,
  Tooltip,
} from '@mantine/core';
import { useDisclosure } from '@mantine/hooks';
import {
  IconFileAlert,
  IconFileDescription,
  IconPlus,
  IconSearch,
  IconTrash,
} from '@tabler/icons-react';
import EmptyState from 'components/states/EmptyState';
import Table from 'components/Table';
import useChildren from 'hooks/children/useChildren';
import { Child } from 'types/generated';

import DrawerChildWriteForm from './components/DrawerChildWriteForm.tsx';
import ModalDeleteChild from './components/ModalDeleteChild.tsx';

const Children = () => {
  const theme = useMantineTheme();

  const [ChildsData, setChildsData] = useState<Child[]>([]);
  const [selectedChild, setSelectedChild] = useState<Child | undefined>(
    undefined,
  );

  const [search, setSearch] = useState<string>('');

  const { data, isSuccess, isLoading, isFetching, isError, error } =
    useChildren();

  const [
    isCreationFormOpened,
    { close: closeCreationForm, open: openCreationForm },
  ] = useDisclosure(false);

  const [
    isDeleteModalOpened,
    { close: closeDeleteModal, open: openDeleteModal },
  ] = useDisclosure(false);

  const handleOpenDeleteModal = (child: Child) => {
    setSelectedChild(child);
    openDeleteModal();
  };
  const handleCloseDeleteModal = () => {
    setSelectedChild(undefined);
    closeDeleteModal();
  };

  const columns = [
    {
      Header: 'Name',
      accessor: 'name',
    },
    {
      Header: 'Surname',
      accessor: 'surname',
    },
    {
      Header: 'Age',
      accessor: 'age',
    },
    {
      Header: 'Gender',
      accessor: 'gender',
    },
    {
      Header: 'Action',
      name: 'action',
      Cell: ({ row }: { row: { original: Child } }) => (
        <Group>
          <Tooltip label='Cancel'>
            <ActionIcon
              variant='light'
              color='red'
              size='lg'
              onClick={() => {
                handleOpenDeleteModal(row.original);
              }}
            >
              <IconTrash size={theme.fontSizes.lg} />
            </ActionIcon>
          </Tooltip>
        </Group>
      ),
    },
  ];

  useEffect(() => {
    if (isSuccess && data?.data) {
      setChildsData(data.data.children);
    }
  }, [isSuccess, data?.data]);

  return (
    <Stack>
      <Flex direction='column'>
        <Title weight={700}>Children</Title>
        <Text color='dimmed'>Children information</Text>
      </Flex>

      <Divider my='md' />

      <Grid columns={10}>
        <Grid.Col sm={10} md={5}>
          <TextInput
            icon={<IconSearch size={theme.fontSizes.lg} />}
            placeholder='Search Child by name'
            value={search}
            onChange={(event) => setSearch(event.currentTarget.value)}
          />
        </Grid.Col>
        <Grid.Col sm={10} md={4}>
          <Group position='right'>
            <Button
              leftIcon={<IconPlus size={theme.fontSizes.lg} />}
              onClick={openCreationForm}
            >
              Add Child
            </Button>
          </Group>
        </Grid.Col>
      </Grid>

      <Paper sx={{ position: 'relative' }}>
        <Table
          data={ChildsData}
          columns={columns}
          isLoading={isLoading || isFetching}
          EmptyState={
            <>
              {isError && (
                <EmptyState
                  mt='xl'
                  title='Error'
                  description={
                    error?.response?.data.message ||
                    'Something went wrong while fetching data.'
                  }
                  Icon={
                    <Avatar radius='100%' size='xl' variant='light' color='red'>
                      <IconFileAlert size={25} />
                    </Avatar>
                  }
                />
              )}
              {isSuccess && ChildsData.length === 0 && (
                <EmptyState
                  mt='xl'
                  title='No Children'
                  description='There are no Children to display.'
                  Icon={
                    <Avatar
                      radius='100%'
                      size='xl'
                      variant='light'
                      color='primary'
                    >
                      <IconFileDescription size={25} />
                    </Avatar>
                  }
                />
              )}
            </>
          }
        />
      </Paper>

      <DrawerChildWriteForm
        opened={isCreationFormOpened}
        onClose={closeCreationForm}
        title='Child Creation'
      />

      <ModalDeleteChild
        child={selectedChild}
        opened={isDeleteModalOpened}
        onClose={handleCloseDeleteModal}
      />
    </Stack>
  );
};

export default Children;
