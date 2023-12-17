import { useState, useEffect } from 'react';

import {
  Grid,
  Title,
  Stack,
  Text,
  Flex,
  Divider,
  TextInput,
  Button,
  Group,
  useMantineTheme,
  SimpleGrid,
  Loader,
  Center,
  Avatar,
} from '@mantine/core';
import { useDisclosure } from '@mantine/hooks';
import { IconFileAlert, IconPlus, IconSearch } from '@tabler/icons-react';
import EmptyState from 'components/states/EmptyState';
import useChildren from 'hooks/parent/useChildren';
import { Child } from 'types/generated/index';

import ChildCard from './components/ChildCard.tsx';
import DrawerChildWriteForm from './components/DrawerChildWriteForm.tsx';
import ModalDeleteChild from './components/ModalDeleteChild.tsx';

const Home = () => {
  const theme = useMantineTheme();

  const [children, setChildren] = useState<Child[]>([]);
  const [selectedChild, setSelectedChild] = useState<Child | undefined>(
    undefined,
  );
  const [search, setSearch] = useState('');

  const { data, isLoading, isSuccess, isError, error } = useChildren();

  const [
    isCreationFormOpened,
    { close: closeCreationForm, open: openCreationForm },
  ] = useDisclosure(false);
  const [isUpdateFormOpened, { close: closeUpdateForm, open: openUpdateForm }] =
    useDisclosure(false);
  const [
    isDeleteModalOpened,
    { close: closeDeleteModal, open: openDeleteModal },
  ] = useDisclosure(false);

  const handleOpenUpdateForm = (child: Child) => {
    setSelectedChild(child);
    openUpdateForm();
  };
  const handleCloseUpdateForm = () => {
    setSelectedChild(undefined);
    closeUpdateForm();
  };

  const handleOpenDeleteModal = (child: Child) => {
    setSelectedChild(child);
    openDeleteModal();
  };
  const handleCloseDeleteModal = () => {
    setSelectedChild(undefined);
    closeDeleteModal();
  };

  useEffect(() => {
    if (isSuccess && data?.data) {
      setChildren(data.data);
    }
  }, [isSuccess, data?.data]);

  return (
    <Stack>
      <Flex direction='column'>
        <Title weight={700}>My Children</Title>
        <Text color='dimmed'>Children information</Text>
      </Flex>

      <Divider my='md' />

      <Grid columns={10}>
        <Grid.Col sm={10} md={4}>
          <TextInput
            icon={<IconSearch size={theme.fontSizes.lg} />}
            placeholder='Search child'
            value={search}
            onChange={(event) => setSearch(event.currentTarget.value)}
          />
        </Grid.Col>
        <Grid.Col sm={10} md={2} />
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

      {isLoading && (
        <Center mt='xl'>
          <Loader />
        </Center>
      )}

      {isSuccess && children.length === 0 && (
        <EmptyState
          title='No Children'
          description='There are no Children to display.'
        />
      )}

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

      <SimpleGrid
        mt='xl'
        spacing='lg'
        breakpoints={[
          { minWidth: 'sm', cols: 2 },
          { minWidth: 'md', cols: 3 },
          { minWidth: 'lg', cols: 4 },
        ]}
        sx={{ position: 'relative' }}
      >
        {children.map((child) => (
          <ChildCard
            // eslint-disable-next-line no-underscore-dangle
            key={child._id}
            img='https://cdn.pixabay.com/photo/2015/06/22/08/40/child-817373_640.jpg'
            name={child.name}
            surname={child.surname}
            age={child.age}
            gender={child.gender}
            handleEdit={() => handleOpenUpdateForm(child)}
            handleDelete={() => handleOpenDeleteModal(child)}
          />
        ))}
      </SimpleGrid>

      <DrawerChildWriteForm
        opened={isCreationFormOpened}
        onClose={closeCreationForm}
        title='Child Creation'
      />

      {selectedChild && (
        <DrawerChildWriteForm
          child={selectedChild}
          opened={isUpdateFormOpened}
          onClose={handleCloseUpdateForm}
          title='Child Edit'
        />
      )}

      <ModalDeleteChild
        child={selectedChild}
        opened={isDeleteModalOpened}
        onClose={handleCloseDeleteModal}
      />
    </Stack>
  );
};

export default Home;
