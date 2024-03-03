import { useEffect, useState } from "react";

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
} from "@mantine/core";
import { useDisclosure } from "@mantine/hooks";
import {
  IconFileAlert,
  IconFileDescription,
  IconInfoCircle,
  IconPlus,
  IconSearch,
  IconTrash,
} from "@tabler/icons-react";
import EmptyState from "components/states/EmptyState";
import Table from "components/Table";
import useChildren from "hooks/children/useChildren";
import { Child } from "types/generated";
import { useTranslation } from "react-i18next";
import DrawerChildWriteForm from "./components/DrawerChildWriteForm.tsx";
import ModalDeleteChild from "./components/ModalDeleteChild.tsx";
import ModalInfoChild from "./components/ModalInfoChild.tsx";
const Children = () => {
  const { t } = useTranslation("children");
  const theme = useMantineTheme();

  const [ChildsData, setChildsData] = useState<Child[]>([]);
  const [selectedChild, setSelectedChild] = useState<Child | undefined>(
    undefined
  );

  const [search, setSearch] = useState<string>("");

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

  const [isInfoModelOpened, { close: closeInfoModal, open: openInfoModal }] =
    useDisclosure(false);

  const handleOpenDeleteModal = (child: Child) => {
    setSelectedChild(child);
    openDeleteModal();
  };
  const handleCloseDeleteModal = () => {
    setSelectedChild(undefined);
    closeDeleteModal();
  };
  const handleOpenInfoModal = (child: Child) => {
    setSelectedChild(child);
    openInfoModal();
  };
  const handleCloseInfoModal = () => {
    setSelectedChild(undefined);
    closeInfoModal();
  };

  const columns = [
    {
      Header: t("firstName"),
      accessor: "name",
    },
    {
      Header: t("lastName"),
      accessor: "surname",
    },
    {
      Header: t("age"),
      accessor: "age",
    },
    {
      Header: t("gender"),
      accessor: "gender",
    },
    {
      Header: t("action"),
      name: "action",
      Cell: ({ row }: { row: { original: Child } }) => (
        <Group>
          <Tooltip label={t("delete")}>
            <ActionIcon
              variant="light"
              color="red"
              size="lg"
              onClick={() => {
                handleOpenDeleteModal(row.original);
              }}
            >
              <IconTrash size={theme.fontSizes.lg} />
            </ActionIcon>
          </Tooltip>
          <Tooltip label="Info">
            <ActionIcon
              variant="light"
              color="blue"
              size="lg"
              onClick={() => {
                handleOpenInfoModal(row.original);
              }}
            >
              <IconInfoCircle size={theme.fontSizes.lg} />
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
      <Flex direction="column">
        <Title weight={700}>{t("title")}</Title>
        <Text color="dimmed">{t("subTitle")}</Text>
      </Flex>

      <Divider my="md" />

      <Grid columns={10}>
        <Grid.Col sm={10} md={5}>
          <TextInput
            icon={<IconSearch size={theme.fontSizes.lg} />}
            placeholder={t("search")}
            value={search}
            onChange={(event) => setSearch(event.currentTarget.value)}
          />
        </Grid.Col>
        <Grid.Col sm={10} md={4}>
          <Group position="right">
            <Button
              leftIcon={<IconPlus size={theme.fontSizes.lg} />}
              onClick={openCreationForm}
            >
              {t("addChild")}
            </Button>
          </Group>
        </Grid.Col>
      </Grid>

      <Paper sx={{ position: "relative" }}>
        <Table
          data={ChildsData}
          columns={columns}
          isLoading={isLoading || isFetching}
          EmptyState={
            <>
              {isError && (
                <EmptyState
                  mt="xl"
                  title="Error"
                  description={error?.response?.data.message || t("error")}
                  Icon={
                    <Avatar radius="100%" size="xl" variant="light" color="red">
                      <IconFileAlert size={25} />
                    </Avatar>
                  }
                />
              )}
              {isSuccess && ChildsData.length === 0 && (
                <EmptyState
                  mt="xl"
                  title={t("noChildren")}
                  description={t("noChildrenDescription")}
                  Icon={
                    <Avatar
                      radius="100%"
                      size="xl"
                      variant="light"
                      color="primary"
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
        title={t("addChild")}
      />

      <ModalDeleteChild
        child={selectedChild}
        opened={isDeleteModalOpened}
        onClose={handleCloseDeleteModal}
      />
      <ModalInfoChild
        child={selectedChild}
        opened={isInfoModelOpened}
        onClose={handleCloseInfoModal}
      />
    </Stack>
  );
};

export default Children;
