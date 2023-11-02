import {
  Stack,
  Paper,
  Title,
  Text,
  TextInput,
  Anchor,
  Checkbox,
  Button,
  PasswordInput,
  ActionIcon,
  createStyles,
  Group,
} from '@mantine/core';
import { useForm } from '@mantine/form';
import { IconChevronLeft } from '@tabler/icons-react';
import { useAuth } from 'contexts/AuthContext';
import { Link } from 'react-router-dom';
import { UserRegistration } from 'types/generated';
import {
  emailValidator,
  passwordValidator,
  rePasswordValidator,
} from 'utils/validations';

const useStyles = createStyles((theme) => ({
  container: {
    display: 'grid',
    gridTemplateColumns: '1fr max-content 1fr',
    gap: theme.spacing.md,
    alignItems: 'center',
    justifyContent: 'center',
  },
}));

interface FormValues {
  firstName: string;
  lastName: string;
  email: string;
  password: string;
  rePassword: string;
  isTermsSigned: boolean;
}

const RegisterParent = () => {
  const { classes, theme } = useStyles();

  const {
    handleRegister,
    isLoginLoading,
  }: {
    handleRegister: (registerPayload: UserRegistration) => void;
    isLoginLoading: boolean;
  } = useAuth();

  const form = useForm<FormValues>({
    initialValues: {
      firstName: '',
      lastName: '',
      email: '',
      password: '',
      rePassword: '',
      isTermsSigned: false,
    },
    validate: {
      email: (value) => emailValidator(value),
      password: (value) => passwordValidator(value),
      rePassword: (value, values) =>
        rePasswordValidator(values.password)(value),
    },
  });

  const handleSubmit = (formValues: FormValues) => {
    const registerPayload = {
      email: formValues.email,
      password: formValues.password,
      firstName: formValues.firstName,
      lastName: formValues.lastName,
      role: 'parent' as UserRegistration['role'],
    };
    handleRegister(registerPayload);
  };

  return (
    <Paper shadow='2xl' radius='md' p='xl' maw={520} w='100%' m='0 auto'>
      <Stack spacing='xl'>
        <div className={classes.container}>
          <ActionIcon component={Link} to='/login'>
            <IconChevronLeft size={theme.fontSizes.lg} />
          </ActionIcon>
          <Title order={4}>Parent Registration</Title>
        </div>

        <form onSubmit={form.onSubmit(handleSubmit)}>
          <Stack>
            <Group noWrap grow>
              <TextInput
                label={
                  <Text weight={700} mb='xs' span>
                    First name
                  </Text>
                }
                placeholder='John'
                required
                {...form.getInputProps('firstName')}
              />
              <TextInput
                label={
                  <Text weight={700} mb='xs' span>
                    Last name
                  </Text>
                }
                placeholder='Doe'
                required
                {...form.getInputProps('lastName')}
              />
            </Group>
            <TextInput
              label={
                <Text weight={600} span>
                  Email address
                </Text>
              }
              placeholder='example@mail.com'
              {...form.getInputProps('email')}
              required
            />

            <PasswordInput
              label={
                <Text weight={600} span>
                  Password
                </Text>
              }
              placeholder='Enter Password'
              {...form.getInputProps('password')}
              required
            />

            <PasswordInput
              label={
                <Text weight={600} span>
                  Password Repeat
                </Text>
              }
              placeholder='Enter Password Repeat'
              {...form.getInputProps('rePassword')}
              required
            />

            <Checkbox
              label={
                <Text>
                  I have read and agree with the{' '}
                  <Anchor
                    component={Link}
                    to='#'
                    color='green'
                    underline
                    sx={{ textDecoration: 'underline' }}
                  >
                    Terms and Conditions
                  </Anchor>
                </Text>
              }
              my='md'
              checked={form.values.isTermsSigned}
              {...form.getInputProps('isTermsSigned')}
              required
            />

            <Button fullWidth type='submit' loading={isLoginLoading}>
              Sign Up
            </Button>

            <Text ta='center'>
              <Text>Already have an account?</Text>
              <Text component={Link} to='/' fw={700} color='green'>
                Log in
              </Text>
            </Text>
          </Stack>
        </form>
      </Stack>
    </Paper>
  );
};

export default RegisterParent;
