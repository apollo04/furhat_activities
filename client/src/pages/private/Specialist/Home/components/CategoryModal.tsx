import useActions from "hooks/specialist/useActions";
import { Center, Loader, Avatar, SegmentedControl, Flex, Grid } from "@mantine/core";
import { IconFileAlert } from "@tabler/icons-react";
import EmptyState from "components/states/EmptyState";
import { useEffect, useState } from "react";
import { Modal } from "@mantine/core";
import { ActionCard } from "./ActionCard";
interface CategoryModalProps {
    opened: boolean;
    onClose: () => void;
    size: "xs" | "sm" | "md" | "lg" | "xl";
    category: string;
    robotInfo?: {
      ip: string;
      name: string;
    }
}

export const CategoryModal = ({ opened, onClose, size, category, robotInfo }: CategoryModalProps): JSX.Element => {
    const [language, setLanguage] = useState("kk");
    const [actions, setActions] = useState<any[]>([]);
    const [categoryData, setCategoryData] = useState<any>({});
    useEffect(() => {
      if (language == 'kk' && categoryData?.actions_kaz) {
        setActions(categoryData?.actions_kaz)
      }
      else if (language == 'ru' && categoryData?.actions_rus) {
        setActions(categoryData?.actions_rus)
      }
    }, [language, categoryData]);

    const { data, isSuccess, isLoading, isFetching, isError, error } =
        useActions(category);
    
    useEffect(() => {
      if (isSuccess && data?.data && opened) {
        setCategoryData(data.data) 
        console.log(data)
      }
  }, [isSuccess, data?.data, opened]);

    return (
        <>
        {isLoading && isFetching && (
        <Center mt="xl">
          <Loader />
        </Center>
      )}
         {isError && (
        <EmptyState
          mt="xl"
          title="Error"
          description={
            error?.response?.data.message ||
            "Something went wrong while fetching data."
          }
          Icon={
            <Avatar radius="100%" size="xl" variant="light" color="red">
              <IconFileAlert size={25} />
            </Avatar>
          }
        />
      )}
        <Modal opened={opened} onClose={onClose} title="Начать упражнение" size={size}>
            <Flex direction='column'>
            <SegmentedControl
                value={language}
                onChange={setLanguage}
                data={[
                { label: 'Қазақша', value: 'ru' },
                { label: 'Русский', value: 'kk' },
                ]}
            />
            <p style={{fontSize: "24px", fontWeight: "600"}}>{category.charAt(0).toUpperCase() + category.slice(1)}</p>
            <Grid style={{
                gap: '1.5rem', 
                paddingTop: "1rem",
                paddingBottom: "2rem",
                paddingRight: "1rem",
                paddingLeft: "1rem",
                }}>
            {actions.map((action) => (
              <ActionCard robotInfo={robotInfo} action={action} />
            ))}
            </Grid>
            </Flex>
            </Modal>
        </>
    );
}