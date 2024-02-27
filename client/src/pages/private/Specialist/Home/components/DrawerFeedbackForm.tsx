import { useEffect, useState } from 'react';

import {
  Button,
  Drawer,
  DrawerProps,
  Group,
  Slider,
  Stack,
  Title,
  Text,
  Select,
} from '@mantine/core';
import { useForm } from '@mantine/form';
import useSubmitFeedback from 'hooks/specialist/useSubmitFeedback';
import {
  showSuccessNotification,
  showErrorNotification,
} from 'utils/notifications';

interface DrawerFeedbackFormProps
  extends Pick<DrawerProps, 'opened' | 'onClose'> {
  categories: any[];
  childId: string;
  title: string;
  isActive: boolean;
}

interface FormValues {
  category: string;
}

const DrawerFeedbackForm = ({
  categories,
  opened,
  onClose,
  childId,
  isActive,
  title,
}: DrawerFeedbackFormProps) => {
  const submitFeedback = useSubmitFeedback(childId);
  const [feedbacks, setFeedbacks] = useState<any>({});
  const [currentFeedback, setCurrentFeedback] = useState<any>({});

  const form = useForm<FormValues>({
    initialValues: {
      category: '',
    },
  });

  const handleClose = () => {
    onClose();
  };

  const handleFullReset = () => {
    form.reset();
    setFeedbacks({});
    setCurrentFeedback({});
  };

  const handleSubmit = (e: any) => {
    e.preventDefault();

    if (childId) {
      submitFeedback.mutate(feedbacks, {
        onSuccess: () => {
          showSuccessNotification('Отзыв успешно сохранен');
          onClose();
        },
        onError: (error) => {
          showErrorNotification(
            'Ошибка при сохранение отзыва',
            error.response?.data.message || error.message,
          );
        },
      });
    }
  };

  const handleCategory = (categoryItem: any, newFeedback: any = null) => {
    if (feedbacks[categoryItem]) {
      setFeedbacks((prev: any) => ({
        ...prev,
        [categoryItem]: {
          ...prev[categoryItem],
          ...(newFeedback || currentFeedback),
        },
      }));
    } else {
      setFeedbacks((prev: any) => ({
        ...prev,
        [categoryItem]: {},
      }));
    }
    setCurrentFeedback({});
  };

  const handleFeedbackChange = (feedback: string, value: number) => {
    setCurrentFeedback((prev: any) => ({
      ...prev,
      [feedback]: value,
    }));

    handleCategory(form.values.category, {
      [feedback]: value,
    });
  };

  const handleCategoryChange = (item: string) => {
    form.setFieldValue('category', item);
    handleCategory(item);
  };

  const currentCategory = categories.find(
    (category) => category.category === form.values.category,
  );

  useEffect(() => {
    if (currentCategory) {
      if (feedbacks[currentCategory.category]) {
        setCurrentFeedback(feedbacks[currentCategory.category]);
      } else {
        setCurrentFeedback([]);
      }
    }
  }, [currentCategory]);

  useEffect(() => {
    if (isActive) {
      handleFullReset();
    }
  }, [isActive]);

  return (
    <Drawer
      opened={opened}
      onClose={handleClose}
      title={<Title order={3}>{title}</Title>}
      sx={{ position: 'relative' }}
    >
      <form onSubmit={handleSubmit}>
        <Stack spacing='xl'>
          <Select
            label='Выберите категорию'
            placeholder='Выберите категорию'
            data={categories.map((category: any) => category.category)}
            value={form.values.category}
            onChange={handleCategoryChange}
          />

          {(currentCategory?.grade_names || []).map((grade_name: any) => (
            <Stack key={grade_name} spacing='xs'>
              <Text>{grade_name}</Text>
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
                value={feedbacks[currentCategory.category][grade_name] || 0}
                onChange={(value) => handleFeedbackChange(grade_name, value)}
              />
            </Stack>
          ))}
        </Stack>

        <Group position='right' mt='xl'>
          <Button
            variant='subtle'
            onClick={handleClose}
            loading={submitFeedback.isLoading}
          >
            Отмена
          </Button>
          <Button type='submit' loading={submitFeedback.isLoading}>
            Сохранить
          </Button>
        </Group>
      </form>
    </Drawer>
  );
};

export default DrawerFeedbackForm;
