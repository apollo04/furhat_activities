import {
  Header as MantineHeader,
  Burger,
  useMantineTheme,
  createStyles,
} from '@mantine/core';
import { useMediaQuery } from '@mantine/hooks';

const useStyles = createStyles((theme) => ({
  container: {
    display: 'grid',
    gridTemplateColumns: '1fr max-content 1fr',
    gap: theme.spacing.md,
  },
}));

interface HeaderProps {
  opened: boolean;
  toggle: () => void;
}

const Header = ({ opened, toggle }: HeaderProps): JSX.Element | undefined => {
  const theme = useMantineTheme();
  const { classes } = useStyles();

  const largeScreen = useMediaQuery(`(min-width: ${theme.breakpoints.md})`);

  if (largeScreen) {
    return undefined;
  }

  return (
    <MantineHeader height={{ base: 60 }} p='md'>
      <div className={classes.container}>
        <Burger opened={opened} onClick={toggle} size='sm' />
      </div>
    </MantineHeader>
  );
};

export default Header;
