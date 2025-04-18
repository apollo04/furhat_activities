import {
  Button,
  // Button,
  createStyles,
  getStylesRef,
  // Group,
  Navbar as MantineNavbar,
  rem,
  Stack,
  Title,
  useMantineTheme,
} from "@mantine/core";
import { useDisclosure } from "@mantine/hooks";
import { useTranslation } from "react-i18next";
import { IconPlus } from "@tabler/icons-react";
// import { IconLogout } from '@tabler/icons-react';
import useCurrentRoute from "hooks/useCurrentRoute";
import useNavbarLinks from "hooks/useNavbarLinks";
import DrawerConnectToRobot from "pages/private/Specialist/Home/components/DrawerConnectToRobot";
import { Link } from "react-router-dom";

const useStyles = createStyles((theme) => ({
  header: {
    paddingBottom: theme.spacing.md,
    marginBottom: `calc(${theme.spacing.md} * 1.5)`,
    borderBottom: `${rem(1)} solid ${theme.colors.gray[2]}`,
  },

  footer: {
    paddingTop: theme.spacing.md,
    marginTop: theme.spacing.md,
    borderTop: `${rem(1)} solid ${theme.colors.gray[2]}`,
  },

  link: {
    ...theme.fn.focusStyles(),

    display: "flex",
    alignItems: "center",
    textDecoration: "none",
    fontSize: theme.fontSizes.sm,
    color: theme.colors.gray[7],
    padding: `${theme.spacing.xs} ${theme.spacing.sm}`,
    borderRadius: theme.radius.md,
    fontWeight: 500,

    "&:hover": {
      backgroundColor: theme.colors.gray[0],
      color: theme.black,

      [`& .${getStylesRef("icon")}`]: {
        color: theme.black,
      },
    },
  },

  linkIcon: {
    ref: getStylesRef("icon"),
    color: theme.colors.gray[6],
    marginRight: theme.spacing.sm,
  },

  linkActive: {
    "&, &:hover": {
      backgroundColor: theme.colors.green[7],
      color: theme.colors.gray[0],
      [`& .${getStylesRef("icon")}`]: {
        color: theme.white,
      },
    },
  },
}));

interface NavbarProps {
  opened: boolean;
}

const Navbar = ({ opened }: NavbarProps) => {
  const { t } = useTranslation("navbar");
  const { classes, cx } = useStyles();
  const theme = useMantineTheme();

  const currentPathname = useCurrentRoute();

  const navbarLinks = useNavbarLinks();

  const [
    isConnectToRobotOpened,
    { close: closeConnectToRobot, open: openConnectToRobot },
  ] = useDisclosure(false);

  const links = navbarLinks.map(({ label, path, Icon }) => (
    <Link
      key={label}
      to={path}
      className={cx(classes.link, {
        [classes.linkActive]: path === currentPathname,
      })}
    >
      <Icon
        className={classes.linkIcon}
        size={theme.fontSizes.lg}
        stroke={1.5}
      />
      <Title order={6} weight={600}>
        {label}
      </Title>
    </Link>
  ));

  return (
    <MantineNavbar
      width={{ md: 300 }}
      hiddenBreakpoint="md"
      hidden={!opened}
      p="xl"
      sx={{ boxShadow: theme.shadows.xl }}
      withBorder={false}
    >
      <MantineNavbar.Section grow>
        <Stack pt="xl" spacing="xs">
          <Button leftIcon={<IconPlus />} onClick={openConnectToRobot}>
            {t("connect")}
          </Button>
          {links}
        </Stack>
        <DrawerConnectToRobot
          opened={isConnectToRobotOpened}
          onClose={closeConnectToRobot}
          title={t("connect")}
        />
      </MantineNavbar.Section>

      {/* <MantineNavbar.Section className={classes.footer}>
        <Button
          variant='subtle'
          color='red'
          fullWidth
          onClick={logout}
          sx={{ display: 'flex', justifyContent: 'flex-start' }}
          size='md'
        >
          <Group spacing='xs'>
            <IconLogout
              color={theme.colors.red[5]}
              size={theme.fontSizes.lg}
              stroke={1.5}
            />
            <Title order={6} weight={600}>
              Logout
            </Title>
          </Group>
        </Button>
      </MantineNavbar.Section> */}
    </MantineNavbar>
  );
};

export default Navbar;
