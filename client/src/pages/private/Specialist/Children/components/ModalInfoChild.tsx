import {
  Box,
  Button,
  Flex,
  Group,
  Modal,
  ModalProps,
  Stack,
  Text,
  Title,
  Divider,
} from "@mantine/core";
import { Child } from "types/generated";
import { Feedbacks } from "types/generated";
interface ModalInfoChildProps extends Pick<ModalProps, "opened" | "onClose"> {
  child?: Child;
}

const ModalInfoChild = ({
  opened,
  onClose,
  child,
}: ModalInfoChildProps): JSX.Element => {
  const infoFields = [
    {
      key: "name",
      value: child?.name,
      label: "Имя",
    },
    {
      key: "surname",
      value: child?.surname,
      label: "Фамилия",
    },
    {
      key: "age",
      value: child?.age,
      label: "Возраст",
    },
    {
      key: "gender",
      value: child?.gender,
      label: "Пол",
    },
    {
      key: "id",
      value: child?.id,
      label: "ID",
    },
  ];
  const feedbacks: Feedbacks = child?.feedbacks || [];
  return (
    <Modal
      opened={opened}
      onClose={onClose}
      title={<Title order={3}>Информация о ребенке</Title>}
      centered
    >
      <Group>
        {infoFields.map((item) => (
          <Flex key={item.key} justify={"space-between"} w={"30rem"}>
            <Text weight={"bold"}>{item.label}</Text>
            <Text>{item.value}</Text>
          </Flex>
        ))}
      </Group>
      <Divider mt={"xl"} />
      <Text align="center" weight={"bold"} mt="lg">
        История занятий
      </Text>
      <Flex direction={"column"}>
        {feedbacks.map((feedback) => (
          <Box key={feedback.id} p={"0.1rem"} m={"1rem"}>
            <Text align="center" weight={"bold"}>
              {new Date(feedback.date).toLocaleDateString()}
            </Text>
            <Stack spacing={4}>
              {Object.entries(feedback.feedback).map(([activity, details]) => (
                <Box key={activity}>
                  <Text weight="bold">
                    {activity.charAt(0).toUpperCase() + activity.slice(1)}
                  </Text>
                  {Object.entries(details).map(([skill, value]) => (
                    <Flex key={skill} w={"15rem"} justify={"space-between"}>
                      <Text>{skill}:</Text>
                      <Text weight={"lighter"}>{value}</Text>
                    </Flex>
                  ))}
                </Box>
              ))}
            </Stack>
          </Box>
        ))}
      </Flex>
    </Modal>
  );
};

export default ModalInfoChild;
