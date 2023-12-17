import { useEffect, useState } from 'react';

import {
  Title,
  Stack,
  Text,
  Flex,
  Divider,
  Group,
  Tooltip,
  ActionIcon,
  Grid,
  TextInput,
  Paper,
  Avatar,
  useMantineTheme,
  Button,
} from '@mantine/core';
import { useDisclosure } from '@mantine/hooks';
import {
  IconFileAlert,
  IconFileDescription,
  IconPencil,
  IconPlus,
  IconSearch,
  IconTrash,
} from '@tabler/icons-react';
import EmptyState from 'components/states/EmptyState';
import Table from 'components/Table';
import useCenters from 'hooks/center/useCenters';
import { Center } from 'types/generated';

import DrawerCenterWriteFrom from './components/DrawerWriteCenterForm.tsx';
import ModalDeleteCenter from './components/ModalDeleteCenter.tsx';

const Home = () => {
  const theme = useMantineTheme();

  const [centersData, setCentersData] = useState<Center[]>([]);
  const [selectedCenter, setSelectedCenter] = useState<Center | undefined>(
    undefined,
  );

  const [search, setSearch] = useState<string>('');

  const { data, isSuccess, isLoading, isFetching, isError, error } =
    useCenters();

  const [
    isCreateModalOpened,
    { close: closeCreateModal, open: openCreateModal },
  ] = useDisclosure(false);

  const [isEditModalOpened, { close: closeEditModal, open: openEditModal }] =
    useDisclosure(false);

  const [
    isDeleteModalOpened,
    { close: closeDeleteModal, open: openDeleteModal },
  ] = useDisclosure(false);

  const handleOpenDeleteModal = (center: Center) => {
    setSelectedCenter(center);
    openDeleteModal();
  };

  const handleCloseDeleteModal = () => {
    setSelectedCenter(undefined);
    closeDeleteModal();
  };

  const handleOpenEditModal = (center: Center) => {
    setSelectedCenter(center);
    openEditModal();
  };

  const handleCloseEditModal = () => {
    setSelectedCenter(undefined);
    closeEditModal();
  };

  const columns = [
    {
      Header: 'Name',
      accessor: 'name',
    },
    {
      Header: 'Country',
      accessor: 'country',
    },
    {
      Header: 'City',
      accessor: 'city',
    },
    {
      Header: 'Street',
      accessor: 'street',
    },
    {
      Header: 'Action',
      name: 'action',
      Cell: ({ row }: { row: { original: Center } }) => (
        <Group>
          <Tooltip label='Cancel'>
            <ActionIcon
              variant='light'
              color='red'
              size='lg'
              onClick={() => handleOpenDeleteModal(row.original)}
            >
              <IconTrash size={theme.fontSizes.lg} />
            </ActionIcon>
          </Tooltip>
          <Tooltip label='Edit'>
            <ActionIcon
              variant='light'
              color='yellow'
              size='lg'
              onClick={() => handleOpenEditModal(row.original)}
            >
              <IconPencil size={theme.fontSizes.lg} />
            </ActionIcon>
          </Tooltip>
        </Group>
      ),
    },
  ];

  useEffect(() => {
    if (isSuccess && data?.data) {
      setCentersData(data.data);
    }
  }, [isSuccess, data?.data]);

  return (
    <Stack>
      <Flex direction='column'>
        <Title weight={700}>Centers</Title>
        <Text color='dimmed'>Centers information</Text>
      </Flex>

      <Divider my='md' />

      <Grid columns={10}>
        <Grid.Col sm={10} md={5}>
          <TextInput
            icon={<IconSearch size={theme.fontSizes.lg} />}
            placeholder='Search Center by name'
            value={search}
            onChange={(event) => setSearch(event.currentTarget.value)}
          />
        </Grid.Col>
        <Grid.Col sm={10} md={4}>
          <Group position='right'>
            <Button
              leftIcon={<IconPlus size={theme.fontSizes.lg} />}
              onClick={openCreateModal}
            >
              Add Center
            </Button>
          </Group>
        </Grid.Col>
      </Grid>

      <Paper sx={{ position: 'relative' }}>
        <Table
          data={centersData}
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
              {isSuccess && centersData.length === 0 && (
                <EmptyState
                  mt='xl'
                  title='No Centers'
                  description='There are no Centers to display.'
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

      <DrawerCenterWriteFrom
        opened={isCreateModalOpened}
        onClose={closeCreateModal}
        title='Create center'
      />

      {selectedCenter && (
        <DrawerCenterWriteFrom
          center={selectedCenter}
          opened={isEditModalOpened}
          onClose={handleCloseEditModal}
          title='Update center'
        />
      )}

      <ModalDeleteCenter
        center={selectedCenter}
        opened={isDeleteModalOpened}
        onClose={handleCloseDeleteModal}
      />
    </Stack>
  );
};

export default Home;
