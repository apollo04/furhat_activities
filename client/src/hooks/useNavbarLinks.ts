import {
  // IconSettings,
  TablerIconsProps,
  IconHome,
  IconUsers,
  IconSettings,
} from "@tabler/icons-react";

type NavbarLink = {
  label: string;
  path: string;
  Icon: (props: TablerIconsProps) => JSX.Element;
};

const specialistItems: NavbarLink[] = [
  {
    label: "Главная",
    path: "/",
    Icon: IconHome,
  },
  {
    label: "Дети",
    path: "/students",
    Icon: IconUsers,
  },
  {
    label: "Настройки",
    path: "/settings",
    Icon: IconSettings,
  },
];

export default function useNavbarLinks(): NavbarLink[] {
  return specialistItems;
}
