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
} from '@mantine/core';
import {
  IconFileAlert,
  IconFileDescription,
  IconSearch,
} from '@tabler/icons-react';
import EmptyState from 'components/states/EmptyState';
import Table from 'components/Table';
import { useAuth } from 'contexts/AuthContext';
import useChildrenByCenter from 'hooks/parent/useChildrenByCenter';
import { Child } from 'types/generated';

const Students = () => {
  const { profile } = useAuth();
  const theme = useMantineTheme();

  const [ChildsData, setChildsData] = useState<Child[]>([]);

  const [search, setSearch] = useState<string>('');

  const { data, isSuccess, isLoading, isFetching, isError, error } =
    useChildrenByCenter(profile?.role_info.center);

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
  ];

  useEffect(() => {
    if (isSuccess && data?.data) {
      setChildsData(data.data);
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
    </Stack>
  );
};

export default Students;
