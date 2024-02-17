import { AxiosError, AxiosResponse } from 'axios';
import { useQuery, UseQueryResult } from 'react-query';
import { axiosUnauthorizedInstance } from 'utils/request';

export default function useActions(): UseQueryResult<
  AxiosResponse<any[]>,
  AxiosError<{ message: string }>
> {
  const getActions = () => {
    return axiosUnauthorizedInstance.get(`/actions`);
  };

  return useQuery(['actions'], getActions);
}
