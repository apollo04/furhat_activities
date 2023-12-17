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
import CenterAutocomplete from 'components/auto-completes/CenterAutocomplete';
import { useAuth } from 'contexts/AuthContext';
import { Link } from 'react-router-dom';
import { DynamicAutoCompleteValue } from 'types';
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
  center: DynamicAutoCompleteValue;
  password: string;
  rePassword: string;
  isTermsSigned: boolean;
}

const RegisterSpecialist = () => {
  const { classes, theme } = useStyles();

  const {
    handleRegister,
    isLoginLoading,
  }: {
    handleRegister: (registerPayload: any) => void;
    isLoginLoading: boolean;
  } = useAuth();

  const form = useForm<FormValues>({
    initialValues: {
      firstName: '',
      lastName: '',
      email: '',
      center: { value: '', label: '' },
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
      name: formValues.firstName,
      surname: formValues.lastName,
      center: formValues.center.value,
      role: 'specialist' as UserRegistration['role'],
    };
    handleRegister(registerPayload);
  };

  const handleCenterChange = (item: DynamicAutoCompleteValue | null) => {
    form.setFieldValue('center', {
      value: item?.value || '',
      label: item?.label || '',
    });
  };

  return (
    <Paper shadow='2xl' radius='md' p='xl' maw={520} w='100%' m='0 auto'>
      <Stack spacing='xl'>
        <div className={classes.container}>
          <ActionIcon component={Link} to='/login'>
            <IconChevronLeft size={theme.fontSizes.lg} />
          </ActionIcon>
          <Title order={4}>Specialist Registration</Title>
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

            <CenterAutocomplete
              label='Center'
              placeholder='Select center'
              value={form.values.center}
              onChange={handleCenterChange}
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

export default RegisterSpecialist;
