import { Stack, Flex, Title, Select } from "@mantine/core";
import { useTranslation } from "react-i18next";

const Settings = (): JSX.Element => {
  const { t, i18n } = useTranslation("settings");

  return (
    <Stack>
      <Flex direction="column">
        <Title weight={700}>{t("title")}</Title>
      </Flex>
      <Select
        data={[
          { value: "kk", label: "Қазақша" },
          { value: "en", label: "English" },
          { value: "ru", label: "Русский" },
        ]}
        label={t("changeLanguage")}
        placeholder={t("languageChoice")}
        onChange={(value) => {
          i18n.changeLanguage(value || "ru");
        }}
      />
    </Stack>
  );
};

export default Settings;
