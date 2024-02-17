import {
  Button,
  Drawer,
  DrawerProps,
  Group,
  Slider,
  Stack,
  Title,
  Text,
} from '@mantine/core';
import { useForm } from '@mantine/form';
import useSubmitFeedback from 'hooks/specialist/useSubmitFeedback';
import {
  showSuccessNotification,
  showErrorNotification,
} from 'utils/notifications';

interface FormValues {
  feedbacks: { [x: string]: number }[];
}

interface DrawerFeedbackFormProps
  extends Pick<DrawerProps, 'opened' | 'onClose'> {
  childId: string;
  title: string;
}

const FEEDBACKS: string[] = [
  'Следование указаням робота',
  'Знание арифметики',
  'Умение читать',
  'Планеты',
  'Профессии',
  'География',
  'Еда',
  'Животные',
  'Супергерои',
  'Праздники и традиции',
  'Обьединение предметов по их свойствам',
  'Составление фраз и предложений',
  'Английский',
];

const DrawerFeedbackForm = ({
  opened,
  onClose,
  childId,
  title,
}: DrawerFeedbackFormProps) => {
  const form = useForm<FormValues>({
    initialValues: {
      feedbacks: FEEDBACKS.map((feedback) => ({ [feedback]: 0 })),
    },
  });
  const submitFeedback = useSubmitFeedback(childId);

  const handleResetAndClose = () => {
    form.reset();
    onClose();
  };

  const handleSubmit = (formValues: FormValues) => {
    if (childId) {
      const resultFeedbacks = formValues.feedbacks.map((feedback) => {
        const key = Object.keys(feedback)[0];
        return {
          feedback_name: key,
          grade: feedback[key],
        };
      });

      submitFeedback.mutate(resultFeedbacks, {
        onSuccess: () => {
          showSuccessNotification('Feedback submitted successfully');
          onClose();
        },
        onError: (error) => {
          showErrorNotification(
            'Feedback submit failed',
            error.response?.data.message || error.message,
          );
        },
      });
    }
  };

  const handleFeedbackChange = (feedback: string, value: number) => {
    form.setFieldValue('feedbacks', [
      ...form.values.feedbacks.filter((f) => !f[feedback]),
      { [feedback]: value },
    ]);
  };

  return (
    <Drawer
      opened={opened}
      onClose={handleResetAndClose}
      title={<Title order={3}>{title}</Title>}
      sx={{ position: 'relative' }}
    >
      <form onSubmit={form.onSubmit(handleSubmit)}>
        <Stack spacing='xl'>
          {FEEDBACKS.map((feedback) => (
            <Stack key={feedback} spacing='xs'>
              <Text>{feedback}</Text>
              <Slider
                color='blue'
                step={10}
                marks={[
                  { value: 0, label: '0' },
                  { value: 10, label: '1' },
                  { value: 20, label: '2' },
                  { value: 30, label: '3' },
                  { value: 40, label: '4' },
                  { value: 50, label: '5' },
                  { value: 60, label: '6' },
                  { value: 70, label: '7' },
                  { value: 80, label: '8' },
                  { value: 90, label: '9' },
                  { value: 100, label: '10' },
                ]}
                name='feedbacks'
                onChange={(value) => handleFeedbackChange(feedback, value)}
              />
            </Stack>
          ))}
        </Stack>

        <Group position='right' mt='xl'>
          <Button
            variant='subtle'
            onClick={handleResetAndClose}
            loading={submitFeedback.isLoading}
          >
            Cancel
          </Button>
          <Button type='submit' loading={submitFeedback.isLoading}>
            Submit
          </Button>
        </Group>
      </form>
    </Drawer>
  );
};

export default DrawerFeedbackForm;
